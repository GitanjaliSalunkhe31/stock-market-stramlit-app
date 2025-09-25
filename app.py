import streamlit as st
from client import API_STOCK_MARKET
import plotly.graph_objects as go

## give page title
st.set_page_config(page_title = "Stock Market App Deployment")

st.title("Stock Market App")
st.subheader("By Admin")
company = st.text_input("Enter Company Name")
 
@st.cache_resource(ttl=3600)
def fetch_data():
    return API_STOCK_MARKET(api_key=st.secrets["API_KEY"])
 
api_stock_market = fetch_data()

@st.cache_data(ttl=3600)
def get_symbol(company_name):
    return api_stock_market.symbol_search(company_name)
 
@st.cache_data(ttl=3600)
def plot_graph(symbol):
    df = api_stock_market.daily_data(symbol)
    fig = api_stock_market.plot_chart(df)
    return fig
 
if company:
    company_data = get_symbol(company)
 
    if company_data:
        symbol_list = list(company_data.keys())
        option = st.selectbox("Select Stock Symbol", symbol_list)
 
        selected_info = company_data[option]
 
        st.success(f"**Company Name:** {selected_info[0]}")
        st.success(f"**Region:** {selected_info[1]}")
        st.success(f"**Currency:** {selected_info[2]}")

        submit = st.button("plot" , type  = "primary")
