def build_xml_element(tag, content, **kwargs):
    attributes = "".join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f"<{tag}{attributes}>{content}</{tag}>"


xml_element = (build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))
print(xml_element)