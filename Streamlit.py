
#cd C:\Users\mauro_000\PycharmProjects\FIrst
#streamlit run Streamlit.py

import streamlit as st
import pickle
from PIL import Image



fig_clusters = Image.open('fig_clusters.png')

fig_lift=Image.open("fig_lift.png")
fig_lift2=Image.open("fig_lift2.png")
fig_cum_gain=Image.open("fig_cum_gain.png")


fig_feat_imp_group = Image.open('fig_feat_imp_group.png')


fig_confusion=Image.open("fig_confusion.png")
fig_pred_plot_tenure=Image.open("fig_pred_plot_tenure.png")
fig_pred_plot_internet=Image.open("fig_pred_plot_internet.png")
fig_pred_plot_montlhy_charges=Image.open("fig_pred_plot_montlhy_charges.png")
fig_pred_plot_contract=Image.open("fig_pred_plot_contract.png")
fig_pred_plot_security=Image.open("fig_pred_plot_security.png")
fig_pred_plot_support=Image.open("fig_pred_plot_support.png")


graph_type={
    "Cluster analysis": fig_clusters,
    "Churn related metrics":[fig_lift,fig_lift2,fig_cum_gain],
    "Feature importance": fig_feat_imp_group,
    "Model predictions": [fig_confusion,fig_pred_plot_tenure,fig_pred_plot_internet,fig_pred_plot_montlhy_charges,fig_pred_plot_contract,
                          fig_pred_plot_security,fig_pred_plot_support]
}


st.title ("Churn analysis project")



st.sidebar.text("Project by Mauro Gioè")
graph=st.selectbox("Select the plot type",["Cluster analysis","Churn related metrics","Feature importance","Model predictions"])


st.header(graph)
if isinstance(graph_type[graph],list):
    for i in range(len(graph_type[graph])):
            st.image(graph_type[graph][i])
else:
    #print(locks[graph])    
    print(graph_type[graph])
    #fig = Image.open(open(graph_type[graph] + ".png"))
    st.image(graph_type[graph])



