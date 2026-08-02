class HTMLNode:

    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""

        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return (
            self,
            self.tag,
            self.value,
            self.children,
            self.props
        )