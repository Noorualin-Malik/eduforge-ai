"""Lightweight ChromaDB memory for EduForge."""

from __future__ import annotations

import json
from typing import Any

import chromadb

from config import settings


class MemoryStore:
    """
    Lightweight wrapper around ChromaDB.

    Stores previously generated learning plans so they can be
    retrieved in future sessions. The application continues to
    function even if memory is unavailable.
    """

    def __init__(
        self,
        path: str | None = None,
        collection_name: str = "learning_plans",
    ) -> None:
        self.client = chromadb.PersistentClient(
            path=path or settings.chroma_path
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def save(
        self,
        topic: str,
        data: dict[str, Any],
    ) -> None:
        """
        Save a learning plan.

        Args:
            topic:
                Learning topic.

            data:
                Structured workflow output.
        """

        self.collection.upsert(
            ids=[topic],
            documents=[json.dumps(data, ensure_ascii=False)],
            metadatas=[{"topic": topic}],
        )

    def load(
        self,
        topic: str,
    ) -> dict[str, Any] | None:
        """
        Retrieve a previously saved learning plan.

        Returns:
            Parsed dictionary if found; otherwise None.
        """

        result = self.collection.get(ids=[topic])

        documents = result.get("documents")

        if not documents:
            return None

        if not documents[0]:
            return None

        return json.loads(documents[0])

    def exists(self, topic: str) -> bool:
        """
        Check whether a topic already exists.
        """

        return self.load(topic) is not None

    def delete(self, topic: str) -> None:
        """
        Delete a stored topic.
        """

        self.collection.delete(ids=[topic])

    def list_topics(self) -> list[str]:
        """
        Return all stored topics.
        """

        result = self.collection.get()

        metadata = result.get("metadatas", [])

        return [
            item["topic"]
            for item in metadata
            if item and "topic" in item
        ]


_memory: MemoryStore | None = None


def get_memory() -> MemoryStore:
    """
    Return a singleton MemoryStore instance.
    """

    global _memory

    if _memory is None:
        _memory = MemoryStore()

    return _memory