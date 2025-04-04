from components.Component import Component


class ItemList(Component):

    @property
    def type_of(self):
        return "Item List"

    def get_text_from_elements(self,timeout = 15,  **kwargs):
       elements =  self.get_all_locator(**kwargs)
       elementsTextList = []
       for element in elements:
           element.inner_html()
           elementsTextList.append(element.inner_html())

       return elementsTextList
