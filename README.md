# 🚀 Enterprise RAG System

> **Build • Retrieve • Reason • Answer**

An Enterprise Retrieval-Augmented Generation (RAG) Assistant built completely from scratch using **Python, OpenAI, FAISS, and GPT**.

---

## 🌟 Project Overview

This project demonstrates how a modern Enterprise AI Assistant retrieves information from company documents using semantic search instead of relying solely on the Large Language Model's internal knowledge.

### The Enterprise RAG pipeline performs the following steps:

- 📄 Loads PDF documents
- ✂️ Splits documents into meaningful chunks
- 🧠 Generates OpenAI embeddings
- 📦 Stores embeddings in a FAISS vector database
- 🔍 Retrieves relevant information using semantic search
- 🤖 Generates grounded answers using GPT

This project was built to understand **RAG from first principles**, without using high-level frameworks like LangChain or LlamaIndex.