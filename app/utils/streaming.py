async def run_graph_stream(graph, initial_state: dict):
    
    async for event in graph.astream(initial_state):
        yield event