import streamlit as st
from pymongo import MongoClient


@st.cache_resource
def get_collection():
    client = MongoClient(
        st.secrets["MONGODB_URI"],
        serverSelectionTimeoutMS=5000,
    )
    client.admin.command("ping")

    database = client[st.secrets.get("MONGODB_DATABASE", "headgenlk")]
    return database[
        st.secrets.get("MONGODB_COLLECTION", "human_evaluations")
    ]


def save_evaluation(evaluation):
    get_collection().insert_one(evaluation)


def save_evaluations(evaluations):
    get_collection().insert_many(evaluations)


def get_evaluations():
    return list(
        get_collection().find({}, {"_id": 0}).sort("timestamp_utc", -1)
    )
