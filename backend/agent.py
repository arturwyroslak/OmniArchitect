import json
import networkx as nx
from typing import Dict, List, Any

class OmniAgent:
    def __init__(self):
        self.graph = nx.DiGraph()

    def analyze_prompt(self, prompt: str) -> Dict[str, Any]:
        """
        Simulates the extraction of entities from a prompt into a Knowledge Graph.
        In a real scenario, this would use an LLM (e.g., GPT-4) to extract nodes/edges.
        """
        # Mock logic for demonstration
        entities = []
        relationships = []
        
        prompt_lower = prompt.lower()
        
        if "kanban" in prompt_lower or "todo" in prompt_lower:
            entities = ["Task", "Column", "User", "Board"]
            relationships = [
                {"source": "Board", "target": "Column", "type": "CONTAINS"},
                {"source": "Column", "target": "Task", "type": "CONTAINS"},
                {"source": "Task", "target": "User", "type": "ASSIGNED_TO"}
            ]
        elif "crm" in prompt_lower:
            entities = ["Customer", "Deal", "Salesperson", "Meeting"]
            relationships = [
                {"source": "Salesperson", "target": "Deal", "type": "MANAGES"},
                {"source": "Customer", "target": "Deal", "type": "HAS"},
                {"source": "Deal", "target": "Meeting", "type": "SCHEDULES"}
            ]
        else:
            entities = ["EntityA", "EntityB"]
            relationships = [{"source": "EntityA", "target": "EntityB", "type": "LINKS_TO"}]

        # Build Graph
        self.graph.clear()
        for e in entities:
            self.graph.add_node(e, type="entity")
        for r in relationships:
            self.graph.add_edge(r["source"], r["target"], relationship=r["type"])

        return {
            "entities": entities,
            "relationships": relationships,
            "graph_stats": {
                "nodes": self.graph.number_of_nodes(),
                "edges": self.graph.number_of_edges()
            }
        }

    def generate_ui_code(self, entities: List[str]) -> str:
        """
        Generates a React component string based on the identified entities.
        """
        main_entity = entities[0] if entities else "Item"
        
        code = f"""
import React, {{ useState }} from 'react';
import {{ Card, CardHeader, CardTitle, CardContent }} from '@/components/ui/card';
import {{ Button }} from '@/components/ui/button';

export default function {main_entity}Dashboard() {{
  const [items, setItems] = useState([
    {{ id: 1, name: 'Sample {main_entity} 1', status: 'Active' }},
    {{ id: 2, name: 'Sample {main_entity} 2', status: 'Pending' }}
  ]);

  return (
    <div className="p-8 bg-gray-50 min-h-screen">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">{main_entity} Manager</h1>
        <Button onClick={{() => alert('Create logic needed')}}>+ New {main_entity}</Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {{items.map(item => (
          <Card key={{item.id}} className="hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle>{{item.name}}</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-gray-500">Status: {{item.status}}</p>
              <div className="mt-4 flex gap-2">
                <Button variant="outline" size="sm">Edit</Button>
                <Button variant="destructive" size="sm">Delete</Button>
              </div>
            </CardContent>
          </Card>
        ))}}
      </div>
      
      <div className="mt-8 p-4 bg-blue-50 rounded-lg border border-blue-100">
        <h3 className="font-semibold text-blue-800">OmniArchitect Insight</h3>
        <p className="text-sm text-blue-600">
          This UI was generated based on the knowledge graph node: <strong>{main_entity}</strong>.
          Backend routes should be generated for <code>GET /{main_entity.lower()}s</code>.
        </p>
      </div>
    </div>
  );
}}
"""
        return code
