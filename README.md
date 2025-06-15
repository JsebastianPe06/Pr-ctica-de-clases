# Practica-de-clases

ignorar

```mermaid
  classDiagram
    class WebSites {
        - name: str
        - main_url: str
        + __init__(name, url)
        + set_html(html, url): str
        + beautiful_soup(html, type_data): Data
        + get_name(): str
        + set_name(new_name, password): str
        + get_url(): str
        + set_url(new_url, password): str
        - save_data()
        - reset_data()
        + export_document(): Document
    }

    class StaticWeb {
        + add_data(new_data)
    }

    class DynamicWeb {
        - opts: Options
        - driver: str
        + add_data(new_data)
        + access_browser(browser): str
    }

    class Wikipedia {
        - name: str = "Wikipedia"
        - urlstr: str = "https:// www. wikipedia. org/"
        + __init__(name, url)
        + search_suggestions(word, language): list[str]
        + create_url(): str
        + export_document(): Document
    }

    class MercadoLibre {
        - name: str = "Mercado Libre"
        - urlstr: str = "https:// www. mercadolibre. com. co/"
        + __init__(name, url)
        + find_data(type, name): str
        + export_document(): Document
    }

    class Citizendium {
        - name: str = "Citizendium"
        - urlstr: str = "https:// www. citizendium. org/"
        + __init__(name, url)
        + create_url(): str
        + export_document(): Document
    }

    class Data {
        - title: str
        - type: str
        - data
        + __init__(title, type)
        + add_data(data)
        + get_type(): str
        + set_type(new_type, password): str
        + get_type(password): str
        + set_data()
    }

    class DataImage {
        + add_data(new_data)
    }

    class DataUrl {
        + add_data(new_data)
    }

    class DataTable {
        + add_data(new_data)
    }

    class DataText {
        + add_data(new_data)
    }

    class Document {
        - Name: str
        - Type: str
        + __init__(name, type)
        + create_document()
        + add_information(new_information)
    }

    class DocumentPdf {
        + create_document()
        + add_information(new_information)
    }

    class DocumentWord {
        + create_document()
        + add_information(new_information)
    }

    class DocumentExcel {
        + create_document()
        + add_information(new_information)
    }

    %% Herencia
    WebSites <|-- StaticWeb
    WebSites <|-- DynamicWeb
    StaticWeb <|-- Wikipedia
    StaticWeb <|-- Citizendium
    DynamicWeb <|-- MercadoLibre

    Data <|-- DataImage
    Data <|-- DataUrl
    Data <|-- DataTable
    Data <|-- DataText

    Document <|-- DocumentPdf
    Document <|-- DocumentWord
    Document <|-- DocumentExcel

    %% Relaciones de composición
    WebSites "1" o-- "*" Data
    WebSites "1" o-- "1" Document
