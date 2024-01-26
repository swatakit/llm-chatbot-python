# Build an Neo4j-backed Chatbot using Python

## Description

This is a repository for a Movie Chatbot backed by neo4j graph database

For a complete walkthrough of this repository, [enrol now](https://graphacademy.neo4j.com/courses/llm-chatbot-python/?ref=github)

If you are entirely new to `LangChain` and `Neo4j`, I recommend exploring the learning resources provided here.

| LangChain | Neo4j |
|-----------|-------|
| [LangChain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) | [Neo4j Fundamentals](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/) |
| [LangChain: Chat with Your Data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/) | [Cypher Fundamentals](https://graphacademy.neo4j.com/courses/cypher-fundamentals/) |
| | [Graph Data Modeling Fundamentals](https://graphacademy.neo4j.com/courses/modeling-fundamentals/) |
| | [Importing CSV data into Neo4j](https://graphacademy.neo4j.com/courses/importing-cypher/) |



## Installation

To run the application, you must install the libraries listed in `requirements.txt`.
```bash
pip install -r requirements.txt
```
## Running the application

Then run the `streamlit run` command to start the app on [http://localhost:8501/](http://localhost:8501/)

```bash
streamlit run bot.py
```

## To setup Neo4j Sandbox account
Follow instruction on [neo4j sandbox](https://neo4j.com/sandbox/)

## Database Schema

```Cypher
call db.schema.visualization()
```

![Data Model](images/data-model.png)

## Cyphe Query Examples

Movies by `Tom Hanks`
```Cypher
MATCH (p:Person)--(m:Movie) WHERE p.name='Tom Hanks' RETURN p,m 
```

![Movie-Tom-Hanks](images/data-model-tom-hanks.png)

Details about `Toy Story`
```Cypher
MATCH (p:Person)--(m:Movie)--(g:Genre) WHERE m.title='Toy Story' RETURN p,m,g
```
![Movie-Toy-Story](images/data-model-toy-story.png)
