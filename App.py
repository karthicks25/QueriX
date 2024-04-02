import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY=<"Your API Key">
genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')


def main():
    st.set_page_config(page_title="SQL Query Generator",page_icon=":robot:")
    st.markdown(
        """ 
            <div style: "text-align:center;">
                <h1> SQL Query Generator </h1>
            </div>
        """,
        unsafe_allow_html=True,
    )
    text_input=st.text_area("Enter your Query in English")
    
    submit=st.button("Generate")
    if submit:
        with st.spinner("Generating SQL Query..."):
            template="""
                    Creating SQL Query using the below text:
                    ```
                        {text_input}
                    ```
                    SQL Query.
            """
            formatted_template=template.format(text_input=text_input)
            st.write(formatted_template)
            response=model.generate_content(formatted_template)
            sql_query=response.text
            sql_query=sql_query.strip().lstrip("```sql").rstrip("```")
            #st.write(sql_query)

            expected_output="""
                    expected response of this SQL query snippet:
                    ```
                        {sql_query}
                    ```
                    Provide sample tabular Response with no explanation:
            """
            expected_output_formatted=expected_output.format(sql_query=sql_query)
            eoutput=model.generate_content(expected_output_formatted)
            eoutput=eoutput.text
            #st.write(eoutput)

            explanation="""
                    Explain this SQL Query
                    ```
                        {sql_query}
                    ```
                    Please provide with simplest of explanation:
            """
            explanation_formatted=explanation.format(sql_query=sql_query)
            explanation=model.generate_content(explanation_formatted)
            explanation=explanation.text
            #st.write(explanation)

            with st.container():
                st.success("Query Generated Successfully!..")
                st.code(sql_query,language='sql')

                st.markdown(eoutput)

                st.markdown(explanation)

main()
