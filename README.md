# Build an Neo4j-backed Chatbot using Python

## Description

This is a repository for a Movie Chatbot backed by neo4j graph database

For a complete walkthrough of this repository, [enrol now](https://graphacademy.neo4j.com/courses/llm-chatbot-python/?ref=github)

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

## To setup Neo4j Sanbox account
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
