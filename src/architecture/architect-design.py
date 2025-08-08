"""
Defines and visualizes the architecture for a multi-agent SOC 2 report analyzer.

This script models a graph-based workflow for analyzing a large document by
splitting it into logical sections and processing them in parallel. It uses
the `networkx` library to build and display the graph structure, which can then
be implemented using a framework like LangGraph.
"""

import networkx as nx
import matplotlib.pyplot as plt
from typing import TypedDict, Literal

# NOTE: The helper classes (ReasoningLLM, AnalysisLLM), the GraphState TypedDict,
# and the SocReportAnalyzer class remain unchanged. The bug was in the
# visualization code within the `main` function.

class ReasoningLLM:
    """Placeholder for a powerful reasoning model like Gemini Pro."""
    def invoke(self, prompt: str) -> str:
        print(f"--- REASONING LLM (Synthesizer) PROMPT ---\n{prompt[:300]}...\n")
        return "This is a synthesized final report based on the analysis of both document parts."

class AnalysisLLM:
    """Placeholder for a fast, efficient model like Gemini Flash."""
    def invoke(self, prompt: str) -> str:
        print(f"--- ANALYSIS LLM (Parallel Node) PROMPT ---\n{prompt[:300]}...\n")
        return "This is a summary of the relevant section."

class GraphState(TypedDict):
    """Represents the state of the analysis graph at any point in time."""
    user_query: str
    full_document: str
    document_part_1: str
    document_part_2: str
    analysis_part_1: str
    analysis_part_2: str
    final_report: str
    route: Literal["split", "full_document"]


class SocReportAnalyzer:
    """Encapsulates the nodes and logic for the SOC 2 report analysis graph."""

    def __init__(self, reasoning_model: ReasoningLLM, analysis_model: AnalysisLLM):
        """Initializes the analyzer with placeholder LLM clients."""
        self.reasoning_model = reasoning_model
        self.analysis_model = analysis_model

    def _split_document(self, doc_text: str) -> tuple[str, str]:
        """Splits the SOC 2 document into two logical parts."""
        split_marker = "SECTION IV – Description of Criteria, AWS Controls, Tests, and Results of Tests"
        parts = doc_text.split(split_marker, 1)
        if len(parts) == 2:
            part1 = parts[0]
            part2 = split_marker + parts[1]
            return part1, part2
        return doc_text, ""

    def router(self, state: GraphState) -> dict:
        """Represents the Router Node."""
        print(">>> Entering Router Node...")
        part1, part2 = self._split_document(state['full_document'])
        return {
            "route": "split",
            "document_part_1": part1,
            "document_part_2": part2
        }

    def analyze_descriptive_part(self, state: GraphState) -> dict:
        """Represents the first Parallel Processing Node."""
        print(">>> Entering Node: Analyze Descriptive Part (Parallel)...")
        prompt = (
            f"User Query: {state['user_query']}\n\n"
            f"Document Section (System Description):\n{state['document_part_1']}\n\n"
            "Based ONLY on the document section provided, extract and summarize "
            "the key information relevant to the user's query."
        )
        analysis = self.analysis_model.invoke(prompt)
        return {"analysis_part_1": analysis}

    def analyze_controls_part(self, state: GraphState) -> dict:
        """Represents the second Parallel Processing Node."""
        print(">>> Entering Node: Analyze Controls Part (Parallel)...")
        prompt = (
            f"User Query: {state['user_query']}\n\n"
            f"Document Section (Controls and Criteria):\n{state['document_part_2']}\n\n"
            "Based ONLY on the document section provided, extract and summarize "
            "the key controls and test results relevant to the user's query."
        )
        analysis = self.analysis_model.invoke(prompt)
        return {"analysis_part_2": analysis}

    def synthesize_report(self, state: GraphState) -> dict:
        """Represents the Aggregator/Report Node."""
        print(">>> Entering Node: Synthesize Report...")
        prompt = (
            f"User Query: {state['user_query']}\n\n"
            f"Analysis of System Description:\n{state['analysis_part_1']}\n\n"
            f"Analysis of System Controls:\n{state['analysis_part_2']}\n\n"
            "Synthesize these two analyses into a single, comprehensive answer "
            "to the user's query."
        )
        report = self.reasoning_model.invoke(prompt)
        return {"final_report": report}


def describe_architecture_graph() -> tuple[nx.DiGraph, dict]:
    """
    Creates a networkx graph and a defined layout to represent the architecture.

    This function defines the nodes, edges, and a fixed node layout for the
    workflow, ensuring a clear and intuitive visualization.

    Returns:
        A tuple containing the networkx.DiGraph object and its layout dictionary.
    """
    graph = nx.DiGraph()
    
    nodes = {
        "start": "START",
        "router": "Router",
        "desc_part": "Analyze\nDescriptive Part",
        "ctrl_part": "Analyze\nControls Part",
        "synthesize": "Synthesize Report",
        "end": "END"
    }

    graph.add_nodes_from(nodes.values())
    
    graph.add_edge(nodes["start"], nodes["router"])
    graph.add_edge(nodes["router"], nodes["desc_part"], label="split above Section IV/4")
    graph.add_edge(nodes["router"], nodes["ctrl_part"], label="split below Section IV/4s")
    graph.add_edge(nodes["desc_part"], nodes["synthesize"])
    graph.add_edge(nodes["ctrl_part"], nodes["synthesize"])
    graph.add_edge(nodes["synthesize"], nodes["end"])
    
    pos = {
        nodes["start"]: (0, 4),
        nodes["router"]: (0, 3),
        nodes["desc_part"]: (-1, 2),
        nodes["ctrl_part"]: (1, 2),
        nodes["synthesize"]: (0, 1),
        nodes["end"]: (0, 0)
    }
    
    return graph, pos


def main():
    """Main entry point for demonstration."""
    
    print("--- ARCHITECTURE VISUALIZATION ---")
    architecture_graph, pos = describe_architecture_graph()
    
    print("\nGraph Nodes:", list(architecture_graph.nodes()))
    print("\nGraph Edges:", list(architecture_graph.edges(data=True)))
    
    try:
        # Styling for the nodes (circles)
        node_opts = {
            "node_size": 4500,
            "node_color": "skyblue",
            "margins": 0.1
        }
        # Styling for the text labels inside the nodes
        label_opts = {"font_size": 8, "font_weight": "bold"}
        # Styling for the edge labels (on the arrows)
        edge_label_opts = {"font_size": 9, "font_color": "darkred"}

        plt.figure(figsize=(10, 8))
        
        # Draw the graph components
        nx.draw_networkx_nodes(architecture_graph, pos, **node_opts)
        nx.draw_networkx_labels(architecture_graph, pos, **label_opts)
        nx.draw_networkx_edges(
            architecture_graph, pos,
            arrowstyle='->', arrowsize=20,
            edge_color='gray'
        )
        
        edge_labels = nx.get_edge_attributes(architecture_graph, 'label')
        nx.draw_networkx_edge_labels(
            architecture_graph, pos,
            edge_labels=edge_labels, **edge_label_opts
        )
        
        plt.title("SOC Report Analyzer LLM Architecture")
        plt.axis('off')
        plt.tight_layout()
        plt.savefig("architecture_diagram.png")
        print("\nSaved corrected architecture diagram to 'architecture_diagram.png'")

    except ImportError:
        print("\nMatplotlib not found. Skipping diagram generation.")
        print("To generate a diagram, run: pip install matplotlib")
    except Exception as e:
        print(f"\nAn error occurred during plot generation: {e}")

if __name__ == '__main__':
    main()
