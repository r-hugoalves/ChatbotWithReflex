"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

def qa(question: str, answer:str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )
    
def chat() -> rx.Component:
    qa_pairs = [
        (
            "Quem é você?",
            "Eu sou um WebApp em Python!"
        ),
        (
            "Construído por quem?",
            "Por Hugo R. Alves"
        )
    ]
    
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )
    
def index() -> rx.Component:
    return rx.container(chat())

app = rx.App()
app.add_page(index)