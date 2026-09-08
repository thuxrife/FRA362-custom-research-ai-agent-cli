import os
import re
import yaml
from pathlib import Path
from typing import Dict, Any

class AgentSpec:
    def __init__(self, role_id: str, name: str, tag: str, description: str, output_dir: str | None, prompt: str):
        self.role_id = role_id
        self.name = name
        self.tag = tag
        self.description = description
        self.output_dir = output_dir
        self.prompt = prompt

    def __repr__(self):
        return f"<AgentSpec {self.role_id} {self.name} {self.tag}>"

def parse_agent_markdown(file_path: Path) -> AgentSpec:
    # Use utf-8-sig to automatically handle any Windows UTF-8 BOM
    text = file_path.read_text(encoding="utf-8-sig").strip()
    frontmatter_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    
    if frontmatter_match:
        yaml_text = frontmatter_match.group(1)
        body = frontmatter_match.group(2).strip()
        metadata = yaml.safe_load(yaml_text) or {}
    else:
        metadata = {}
        body = text.strip()

    # Determine fallback role_id from filename (e.g., 1-2-researcher -> 1.2)
    filename_stem = file_path.stem
    fallback_id = ""
    stem_parts = filename_stem.split("-")
    if len(stem_parts) >= 2 and stem_parts[0].isdigit() and stem_parts[1].isdigit():
        fallback_id = f"{stem_parts[0]}.{stem_parts[1]}"

    role_id = str(metadata.get("role_id", "")).strip() or fallback_id

    return AgentSpec(
        role_id=role_id,
        name=str(metadata.get("name", filename_stem)),
        tag=str(metadata.get("tag", f"({filename_stem})")),
        description=str(metadata.get("description", "")),
        output_dir=metadata.get("output_dir"),
        prompt=body
    )

def load_all_agents(agents_dir: str = "agents") -> Dict[str, AgentSpec]:
    path = Path(agents_dir)
    agents = {}
    if not path.exists():
        return agents
    for md_file in sorted(path.glob("*.md")):
        spec = parse_agent_markdown(md_file)
        if spec.role_id:
            agents[spec.role_id] = spec
            # Also register normalized alias (e.g. "1.2" and "1-2")
            agents[spec.role_id.replace('.', '-')] = spec
    return agents

if __name__ == "__main__":
    loaded = load_all_agents()
    print(f"Successfully loaded {len(loaded)} agent keys from markdown:")
    for role_id, spec in loaded.items():
        print(f" - [{role_id}] {spec.name} -> {spec.tag} (Output: {spec.output_dir})")
