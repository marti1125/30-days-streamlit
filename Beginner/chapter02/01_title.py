import streamlit as st

st.header("YouTube Analytics Dashboard")
st.subheader("Apress")
st.title("YouTube Analytics Dashboard", anchor="Apress")
st.caption("Caption Apress")

st.text("Text Apress")
st.text("Text Apress second line")

st.markdown("### Hello")
st.markdown("*Strong*")

st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")

st.subheader("""Python Code""")
code = """def hello():
print("Hello, Streamlit!")"""
st.code(code, language="python")

st.subheader("""Java Code""")
st.code("""public class GFG {
    public static void main(String args[])
    {
        System.out.println("Hello World");
    }
}""", language="java")

st.subheader("""JavaScript Code""")
st.code(""" <p id="demo"></p>
<script>
try {
adddlert("Welcome guest!");
}
catch(err) {
document.getElementById("demo").innerHTML = err.message;
}
</script> """, language="javascript")
