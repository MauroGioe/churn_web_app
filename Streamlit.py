
#cd C:\Users\mauro_000\PycharmProjects\FIrst
#streamlit run Streamlit.py

import streamlit as st
import pickle

fig_clusters=pickle.load(open("Clusters.pickle","rb"))


fig_lift=pickle.load(open("Lift_chart.pickle","rb"))
fig_lift2=pickle.load(open("Lift_chart2.pickle","rb"))
fig_cum_gain=pickle.load(open("Cumulative_gain.pickle","rb"))

fig_feat_imp=pickle.load(open("Feature_importance.pickle","rb"))
fig_feat_imp_group=pickle.load(open("Feature_importance_group.pickle","rb"))

fig_confusion=pickle.load(open("Conf_matrix.pickle","rb"))
fig_pred_plot_tenure=pickle.load(open("Predi_boxplot_tenure.pickle","rb"))
fig_pred_plot_internet=pickle.load(open("Predi_boxplot_internet.pickle","rb"))
fig_pred_plot_montlhy_charges=pickle.load(open("Predi_boxplot_montlhy_charges.pickle","rb"))
fig_pred_plot_contract=pickle.load(open("Predi_boxplot_contract.pickle","rb"))
fig_pred_plot_security=pickle.load(open("Predi_boxplot_Online_security.pickle","rb"))
fig_pred_plot_support=pickle.load(open("Predi_boxplot_techsupport.pickle","rb"))
graph_type={
    "Cluster analysis":fig_clusters,
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
        st.pyplot(graph_type[graph][i])
else:
    st.pyplot(graph_type[graph])



