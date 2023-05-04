from dataclasses import dataclass, field


@dataclass
class Project:
    """Simple object representation of a project."""

    name: str
    site: str
    owner: str
    tag: str
    tickets: list[str] = field(default_factory=list)
    description: str | None = None

    @property
    def url(self):
        if self.site == "github":
            return f"https://github.com/{self.name}/"
        if self.site == "pagure.io":
            return f"https://pagure.io/{self.name}/"
        if self.site == "gitlab.com":
            return f"https://gitlab.com/{self.name}/"

    @property
    def email(self):
        if "@" in self.owner:
            return self.owner
        else:
            return f"{self.owner}@fedoraproject.org"

    @property
    def group(self):
        if "/" not in self.name:
            return None
        return self.name.split("/")[0]

    @property
    def repo_name(self):
        if "/" not in self.name:
            return self.name
        return self.name.split("/", 1)[1]


@dataclass
class Ticket:
    """Simple object representation of a ticket."""

    id: str
    url: str
    title: str
    status: str
    created_at: str
    updated_at: str
    labels: list[str] = field(default_factory=list)
    assignees: list[str] = field(default_factory=list)
    type: str = ""
    component: str = ""