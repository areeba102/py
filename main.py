import streamlit as st





conversion_factors = {
    'mm': {'cm': 0.1, 'm': 0.001, 'km': 0.000001, 'in': 0.0393701, 'ft': 0.00328084},
    'cm': {'mm': 10, 'm': 0.01, 'km': 0.00001, 'in': 0.393701, 'ft': 0.0328084},
    'm': {'mm': 1000, 'cm': 100, 'km': 0.001, 'in': 39.3701, 'ft': 3.28084},
    'km': {'mm': 1000000, 'cm': 100000, 'm': 1000, 'in': 39370.1, 'ft': 3280.84},
    'in': {'mm': 25.4, 'cm': 2.54, 'm': 0.0254, 'km': 0.0000254, 'ft': 0.0833333},
    'ft': {'mm': 304.8, 'cm': 30.48, 'm': 0.3048, 'km': 0.0003048, 'in': 12}
}

def convert_length(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    else:
        return value * conversion_factors[from_unit][to_unit]







container = st.container()


with container:
    st.markdown("<h1 style='text-align: center; color:rgb(255, 0, 0);'>Length Unit Converter</h1>", unsafe_allow_html=True)

          
    st.write("Select the unit you want to convert from:")
    from_unit = st.selectbox("", ['mm', 'cm', 'm', 'km', 'in', 'ft'], key="from_unit")


    st.write("Enter the value you want to convert:")
    value = st.number_input("", min_value=0.0)

    st.write("Select the unit you want to convert to:")
    to_unit = st.selectbox("", ['mm', 'cm', 'm', 'km', 'in', 'ft'], key="to_unit")

    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
        # Display the result
        st.markdown(f"<h2 style='text-align: center; color: #ff0000;'>{value} {from_unit} is equal to {result} {to_unit}</h2>", unsafe_allow_html=True)


