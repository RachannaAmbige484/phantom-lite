import streamlit as st

from scanner import extract_endpoints

from comparator import (
    load_openapi,
    extract_documented_endpoints,
    compare_endpoints
)

from rag import (
    load_corpus,
    load_model,
    generate_embeddings,
    retrieve_similar
)

from llm import generate_documentation


# Configure the application
st.set_page_config(
    page_title="PHANTOM Lite",
    page_icon="👻",
    layout="wide"
)


# Application title
st.title("👻 PHANTOM LITE")

st.subheader("AI-Powered API Discovery and Documentation System")

st.write(
    "Discover undocumented API endpoints "
    "and generate AI-powered documentation suggestions."
)


# Display project information
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Project", "PHANTOM Lite")

with col2:
    st.metric("Technology", "Python + RAG")

with col3:
    st.metric("AI Model", "Groq")


# File upload section
st.divider()

st.header("API Analysis")

source_file = st.file_uploader(
    "Upload Python Source Code",
    type=["py"]
)

openapi_file = st.file_uploader(
    "Upload OpenAPI JSON",
    type=["json"]
)


# Analyze API button
st.divider()

if st.button("🚀 Analyze API", use_container_width=True):

    if source_file is not None and openapi_file is not None:

        st.success("Both files uploaded successfully!")

        # Save uploaded Python source
        source_code = source_file.getvalue().decode("utf-8")

        with open("uploaded_source.py", "w", encoding="utf-8") as file:
            file.write(source_code)

        # Save uploaded OpenAPI documentation
        openapi_content = openapi_file.getvalue()

        with open("uploaded_openapi.json", "wb") as file:
            file.write(openapi_content)

        st.success("Files are ready for PHANTOM analysis!")

        # Run PHANTOM scanner
        discovered_endpoints = extract_endpoints("uploaded_source.py")

        # Load uploaded OpenAPI documentation
        spec = load_openapi("uploaded_openapi.json")

        if spec:

            # Extract documented endpoints
            documented_endpoints = extract_documented_endpoints(spec)

            # Compare endpoints
            missing_endpoints = compare_endpoints(
                discovered_endpoints,
                documented_endpoints
            )

            # Display analysis results
            st.divider()
            st.header("📊 Analysis Results")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Discovered Endpoints",
                len(discovered_endpoints)
            )

            col2.metric(
                "Documented Endpoints",
                len(documented_endpoints)
            )

            col3.metric(
                "Undocumented Endpoints",
                len(missing_endpoints)
            )

            # Display undocumented endpoints
            st.subheader("Undocumented Endpoints")

            if missing_endpoints:

                for method, path in missing_endpoints:
                    st.error(f"{method} {path}")

                # RAG + Groq documentation generation
                st.divider()
                st.header("🤖 AI Documentation Suggestions")

                with st.spinner("Loading RAG knowledge base..."):

                    corpus = load_corpus("corpus.json")
                    model = load_model()

                    descriptions, embeddings = generate_embeddings(
                        model,
                        corpus
                    )

                # Process each undocumented endpoint
                for method, path in missing_endpoints:

                    st.subheader(f"{method} {path}")

                    query = f"{method} {path} API endpoint"

                    similar_examples = retrieve_similar(
                        query,
                        model,
                        descriptions,
                        embeddings
                    )

                    with st.spinner("Generating AI documentation..."):

                        suggestion = generate_documentation(
                            method,
                            path,
                            similar_examples
                        )

                    st.markdown(suggestion)

                    st.divider()

            else:

                st.success("No undocumented endpoints found!")

            st.write("Python File:", source_file.name)
            st.write("OpenAPI File:", openapi_file.name)

            st.success("PHANTOM Analysis Completed!")

        else:

            st.error("Unable to analyze the OpenAPI file. Please check its contents.")

    else:

        st.warning("Please upload both files before analysis.")