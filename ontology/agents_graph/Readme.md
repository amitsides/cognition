<mxfile host="app.diagrams.net" modified="2025-10-19T14:23:53.000Z" agent="5.0" etag="refined_hmas_a2a" version="22.1.18" type="embed">
  <diagram id="A2A_HMAS_Unified_Diagram" name="A2A/ADK/HMAS Integration Architecture">
    <mxGraphModel dx="1600" dy="950" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="1200" background="#ffffff" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- A2A Protocol Layer -->
        <mxCell id="A2ALayerLabel" value="&lt;b&gt;A2A PROTOCOL LAYER&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="80" y="40" width="200" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="AgentCard" value="&lt;u&gt;&lt;b&gt;AgentCard&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ name: str&#xa;+ description: str&#xa;+ version: str&#xa;+ url: str&#xa;+ rpc_endpoint: str&#xa;+ doc_url: str&#xa;+ default_input_modes: list&#xa;+ default_output_modes: list&#xa;+ supports_auth: bool&#xa;--&#xa;+ get_agent_card()&#xa;+ build_from_agent(agent: BaseAgent)" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="80" y="80" width="220" height="240" as="geometry" />
        </mxCell>
        
        <mxCell id="AgentSkill" value="&lt;u&gt;&lt;b&gt;AgentSkill&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ id: str&#xa;+ name: str&#xa;+ description: str&#xa;+ examples: list&#xa;+ input_modes: list&#xa;+ output_modes: list&#xa;+ tags: list&#xa;--&#xa;+ matches_requirement(tag: str): bool" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="360" y="80" width="220" height="160" as="geometry" />
        </mxCell>
        
        <mxCell id="SkillTypes" value="&lt;u&gt;&lt;b&gt;&amp;lt;&amp;lt;enumeration&amp;gt;&amp;gt;&lt;/b&gt;&lt;/u&gt;&#xa;&lt;b&gt;SkillType&lt;/b&gt;&#xa;--&#xa;+ MODEL_SKILL&#xa;+ TOOL_SKILL&#xa;+ PLANNING_SKILL&#xa;+ CODE_EXECUTION_SKILL&#xa;+ ORCHESTRATION_SKILL" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="360" y="260" width="220" height="120" as="geometry" />
        </mxCell>
        
        <mxCell id="AgentCapabilities" value="&lt;u&gt;&lt;b&gt;AgentCapabilities&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ streaming: bool&#xa;+ push_notifications: bool&#xa;+ batch_processing: bool" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="80" y="360" width="220" height="100" as="geometry" />
        </mxCell>
        
        <mxCell id="SecurityScheme" value="&lt;u&gt;&lt;b&gt;SecurityScheme&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ type: str (apiKey, oauth2)&#xa;+ description: str&#xa;+ location: str" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#f8cecc;strokeColor=#b85450;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="80" y="500" width="220" height="100" as="geometry" />
        </mxCell>
        
        <!-- ADK Agent Layer -->
        <mxCell id="ADKLayerLabel" value="&lt;b&gt;ADK AGENT LAYER&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="640" y="40" width="200" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="BaseAgent" value="&lt;u&gt;&lt;b&gt;BaseAgent&lt;/b&gt;&lt;/u&gt;&#xa;&lt;i&gt;&amp;lt;&amp;lt;abstract&amp;gt;&amp;gt;&lt;/i&gt;&#xa;--&#xa;+ name: str&#xa;+ description: str&#xa;+ sub_agents: list&lt;BaseAgent&gt;&#xa;--&#xa;+ run(input: str): str&#xa;+ canonical_tools(): list" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="640" y="80" width="220" height="160" as="geometry" />
        </mxCell>
        
        <mxCell id="LlmAgent" value="&lt;u&gt;&lt;b&gt;LlmAgent&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ tools: list&lt;Tool&gt;&#xa;+ planner: Planner&#xa;+ code_executor: CodeExecutor&#xa;+ instructions: str&#xa;--&#xa;+ build_llm_skills(): list&lt;AgentSkill&gt;" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="640" y="280" width="220" height="140" as="geometry" />
        </mxCell>
        
        <mxCell id="SequentialAgent" value="&lt;u&gt;&lt;b&gt;SequentialAgent&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ orchestration_pattern: &quot;sequential&quot;&#xa;--&#xa;+ execute_in_sequence()" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="920" y="280" width="200" height="100" as="geometry" />
        </mxCell>
        
        <mxCell id="ParallelAgent" value="&lt;u&gt;&lt;b&gt;ParallelAgent&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ orchestration_pattern: &quot;parallel&quot;&#xa;--&#xa;+ execute_in_parallel()" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="920" y="400" width="200" height="100" as="geometry" />
        </mxCell>
        
        <mxCell id="LoopAgent" value="&lt;u&gt;&lt;b&gt;LoopAgent&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ orchestration_pattern: &quot;loop&quot;&#xa;--&#xa;+ execute_iteratively()" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#ffe6cc;strokeColor=#d79b00;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="920" y="520" width="200" height="100" as="geometry" />
        </mxCell>
        
        <!-- HMAS Graph Layer -->
        <mxCell id="HMASLayerLabel" value="&lt;b&gt;HMAS GRAPH LAYER&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="80" y="650" width="200" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="AgentNode" value="&lt;u&gt;&lt;b&gt;AgentNode&lt;/b&gt;&lt;/u&gt;&#xa;&lt;i&gt;(Layer 1: Agent Layer)&lt;/i&gt;&#xa;--&#xa;+ uri: str&#xa;+ name: str&#xa;+ state: AgentState&#xa;+ workload: int&#xa;+ performance_score: float&#xa;+ wraps_agent: BaseAgent&#xa;+ exposes_card: AgentCard&#xa;--&#xa;+ can_handle_task(task: TaskCard): bool" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="80" y="690" width="250" height="200" as="geometry" />
        </mxCell>
        
        <mxCell id="ClusterNode" value="&lt;u&gt;&lt;b&gt;ClusterNode&lt;/b&gt;&lt;/u&gt;&#xa;&lt;i&gt;(Layer 2: Cluster Layer)&lt;/i&gt;&#xa;--&#xa;+ uri: str&#xa;+ formation_time: datetime&#xa;+ cluster_size: int&#xa;+ coordination_mode: str&#xa;+ required_skills: list&lt;AgentSkill&gt;&#xa;--&#xa;+ add_agent(agent: AgentNode)&#xa;+ dissolve_cluster()" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="380" y="690" width="250" height="180" as="geometry" />
        </mxCell>
        
        <mxCell id="TargetNode" value="&lt;u&gt;&lt;b&gt;TargetNode&lt;/b&gt;&lt;/u&gt;&#xa;&lt;i&gt;(Layer 3: Target Layer)&lt;/i&gt;&#xa;--&#xa;+ uri: str&#xa;+ objective: str&#xa;+ priority: int&#xa;+ deadline: datetime&#xa;+ reward_value: float&#xa;+ required_skills: list&lt;AgentSkill&gt;&#xa;--&#xa;+ assign_to_cluster(cluster: ClusterNode)" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="680" y="690" width="280" height="180" as="geometry" />
        </mxCell>
        
        <mxCell id="CooperationEdge" value="&lt;u&gt;&lt;b&gt;CooperationEdge&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ source: GraphNode&#xa;+ target: GraphNode&#xa;+ edge_weight: float (0.0-1.0)&#xa;+ edge_type: EdgeType&#xa;+ trust_score: float&#xa;+ collaboration_count: int&#xa;+ last_interaction: datetime&#xa;+ shared_skills: list&lt;AgentSkill&gt;&#xa;--&#xa;+ update_weight(outcome: HandoffOutcome)&#xa;+ strengthen_edge()&#xa;+ weaken_edge()" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="80" y="920" width="280" height="220" as="geometry" />
        </mxCell>
        
        <mxCell id="EdgeTypes" value="&lt;u&gt;&lt;b&gt;&amp;lt;&amp;lt;enumeration&amp;gt;&amp;gt;&lt;/b&gt;&lt;/u&gt;&#xa;&lt;b&gt;EdgeType&lt;/b&gt;&#xa;--&#xa;+ AGENT_TO_AGENT&#xa;+ AGENT_TO_CLUSTER&#xa;+ CLUSTER_TO_TARGET&#xa;+ SUB_AGENT_LINK" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="400" y="920" width="200" height="120" as="geometry" />
        </mxCell>
        
        <!-- Task Card Layer -->
        <mxCell id="TaskCardLabel" value="&lt;b&gt;TASK HANDOFF LAYER&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="1000" y="650" width="200" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="TaskCard" value="&lt;u&gt;&lt;b&gt;TaskCard&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ card_id: str&#xa;+ task_type: str&#xa;+ context: str&#xa;+ required_skills: list&lt;AgentSkill&gt;&#xa;+ current_holder: AgentNode&#xa;+ handoff_history: list&lt;HandoffEvent&gt;&#xa;+ creation_time: datetime&#xa;+ completion_criteria: str&#xa;+ status: TaskStatus&#xa;+ preferred_agent: AgentCard&#xa;--&#xa;+ handoff_to(agent: AgentNode): HandoffEvent&#xa;+ find_capable_agent(): AgentNode&#xa;+ complete_task()" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#fce5cd;strokeColor=#d8a436;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1000" y="690" width="280" height="260" as="geometry" />
        </mxCell>
        
        <mxCell id="HandoffEvent" value="&lt;u&gt;&lt;b&gt;HandoffEvent&lt;/b&gt;&lt;/u&gt;&#xa;--&#xa;+ sequence_number: int&#xa;+ timestamp: datetime&#xa;+ from_agent: AgentNode&#xa;+ to_agent: AgentNode&#xa;+ outcome: HandoffOutcome&#xa;+ reason: str&#xa;+ edge_weight_update: float&#xa;--&#xa;+ record_success()&#xa;+ record_failure()&#xa;+ update_graph_topology()" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#fce5cd;strokeColor=#d8a436;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="1000" y="980" width="280" height="180" as="geometry" />
        </mxCell>
        
        <!-- Graph Operators -->
        <mxCell id="OperatorsLabel" value="&lt;b&gt;GRAPH OPERATORS&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="640" y="920" width="200" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="GraphOperator" value="&lt;u&gt;&lt;b&gt;GraphOperator&lt;/b&gt;&lt;/u&gt;&#xa;&lt;i&gt;&amp;lt;&amp;lt;abstract&amp;gt;&amp;gt;&lt;/i&gt;&#xa;--&#xa;+ triggered_by: str&#xa;+ effect: str&#xa;--&#xa;+ execute(graph: HMASGraph)&#xa;+ can_apply(): bool" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="640" y="960" width="240" height="140" as="geometry" />
        </mxCell>
        
        <mxCell id="FormClusterOp" value="&lt;b&gt;FormClusterOperator&lt;/b&gt;&#xa;--&#xa;+ form_cluster(agents: list)" style="swimlane;fontStyle=0;align=left;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="920" y="960" width="180" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="DissolveClusterOp" value="&lt;b&gt;DissolveClusterOperator&lt;/b&gt;&#xa;--&#xa;+ dissolve_cluster(cluster: ClusterNode)" style="swimlane;fontStyle=0;align=left;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="920" y="1040" width="200" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="AssignAgentOp" value="&lt;b&gt;AssignAgentOperator&lt;/b&gt;&#xa;--&#xa;+ assign_to_cluster(agent, cluster)" style="swimlane;fontStyle=0;align=left;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="1140" y="960" width="200" height="60" as="geometry" />
        </mxCell>
        
        <mxCell id="AllocateTargetOp" value="&lt;b&gt;AllocateTargetOperator&lt;/b&gt;&#xa;--&#xa;+ allocate_target(cluster, target)" style="swimlane;fontStyle=0;align=left;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="1140" y="1040" width="200" height="60" as="geometry" />
        </mxCell>
        
        <!-- SPARQL Service -->
        <mxCell id="SPARQLLabel" value="&lt;b&gt;GRAPH SERVICES&lt;/b&gt;" style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=14;fontStyle=1" vertex="1" parent="1">
          <mxGeometry x="400" y="1070" width="200" height="30" as="geometry" />
        </mxCell>
        
        <mxCell id="HMASGraphBuilder" value="&lt;u&gt;&lt;b&gt;HMASGraphBuilder&lt;/b&gt;&lt;/u&gt;&#xa;&lt;i&gt;&amp;lt;&amp;lt;service&amp;gt;&amp;gt;&lt;/i&gt;&#xa;--&#xa;+ sparql_endpoint: str&#xa;+ graph: RDFGraph&#xa;--&#xa;+ register_agent(agent: BaseAgent): AgentNode&#xa;+ build_agent_card(agent: BaseAgent): AgentCard&#xa;+ map_skills_to_graph(card: AgentCard)&#xa;+ map_sub_agent_hierarchy(agent: BaseAgent)&#xa;+ route_task_card(task: TaskCard): AgentNode&#xa;+ form_cluster(target: TargetNode): ClusterNode&#xa;+ execute_sparql_query(query: str): Result&#xa;+ execute_sparql_update(query: str)" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#e1d5e7;strokeColor=#9673a6;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="400" y="1110" width="320" height="240" as="geometry" />
        </mxCell>
        
        <mxCell id="AgentCardBuilder" value="&lt;u&gt;&lt;b&gt;AgentCardBuilder&lt;/b&gt;&lt;/u&gt;&#xa;&lt;i&gt;&amp;lt;&amp;lt;builder&amp;gt;&amp;gt;&lt;/i&gt;&#xa;--&#xa;+ agent: BaseAgent&#xa;+ rpc_url: str&#xa;+ capabilities: AgentCapabilities&#xa;--&#xa;+ build(): AgentCard&#xa;+ build_primary_skills(): list&lt;AgentSkill&gt;&#xa;+ build_sub_agent_skills(): list&lt;AgentSkill&gt;&#xa;+ build_tool_skills(): list&lt;AgentSkill&gt;" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="760" y="1110" width="280" height="200" as="geometry" />
        </mxCell>
        
        <!-- Relationships -->
        
        <!-- AgentCard contains AgentSkills -->
        <mxCell id="CardSkillRel" value="" style="endArrow=diamond;startArrow=none;html=1;endFill=1;exitX=1;exitY=0.25;entryX=0;entryY=0.5;" edge="1" parent="1" source="AgentCard" target="AgentSkill">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="300" y="150" as="sourcePoint" />
            <mxPoint x="360" y="150" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="CardSkillLabel" value="has skills" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;" vertex="1" connectable="0" parent="CardSkillRel">
          <mxGeometry x="-0.2" y="1" relative="1" as="geometry">
            <mxPoint x="5" y="-9" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="CardSkillMult" value="1..*" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="320" y="140" width="30" height="20" as="geometry" />
        </mxCell>
        
        <!-- AgentCard has AgentCapabilities -->
        <mxCell id="CardCapRel" value="" style="endArrow=diamond;startArrow=none;html=1;endFill=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="AgentCard" target="AgentCapabilities">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="190" y="320" as="sourcePoint" />
            <mxPoint x="190" y="360" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="CardCapLabel" value="declares" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;" vertex="1" connectable="0" parent="CardCapRel">
          <mxGeometry x="-0.2" y="1" relative="1" as="geometry">
            <mxPoint x="25" y="-5" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="CardCapMult" value="1" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="165" y="330" width="20" height="20" as="geometry" />
        </mxCell>
        
        <!-- AgentCard has SecurityScheme -->
        <mxCell id="CardSecRel" value="" style="endArrow=diamond;startArrow=none;html=1;endFill=1;exitX=0.5;exitY=1;entryX=0.5;entryY=0;" edge="1" parent="1" source="AgentCapabilities" target="SecurityScheme">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="190" y="460" as="sourcePoint" />
            <mxPoint x="190" y="500" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="CardSecLabel" value="secured by" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;" vertex="1" connectable="0" parent="CardSecRel">
          <mxGeometry x="-0.2" y="1" relative="1" as="geometry">
            <mxPoint x="30" y="-5" as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="CardSecMult" value="0..*" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;fontSize=10;" vertex="1" parent="1">
          <mxGeometry x="165" y="470" width="30" height="20" as="geometry" />
        </mxCell>
        
        <!-- BaseAgent inheritance -->
        <mxCell id="LlmInherit" value="" style="endArrow=block;startArrow=none;html=1;endFill=0;exitX=0.5;exitY=0;entryX=0.5;entryY=1;" edge="1" parent="1" source="LlmAgent" target="BaseAgent">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="750" y="280" as="sourcePoint" />
            <mxPoint x="750" y="240" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        
        <mxCell id="SeqInherit" value="" style="endArrow=block;startArrow=none;html=1;endFill=0;exitX=0;exitY=0.5;entryX=1;entryY=0.5;" edge="1" parent="1" source="SequentialAgent" target="BaseAgent">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="920" y="330" as="sourcePoint" />
            <mxPoint x="860" y="160" as="targetPoint" />
            <Array as="points">
              <mxPoint x="880" y="330" />
              <mxPoint x="880" y="160" />
            </Array>
          </mxGeometry>
        </mxCell>