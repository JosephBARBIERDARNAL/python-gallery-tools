def define_meta_data(chartType, description, family, keywords, seoDescription, slug, title):
    meta_data_template = f'''
    "metadata": {{\n
        "chartType": "{chartType}",
        "description": "{description}",
        "family": "{family}",
        "kernelspec": {{
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        }},
        "keywords": "{keywords}",
        "language_info": {{
            "codemirror_mode": {{
                "name": "ipython",
                "version": 3
            }},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.13"
        }},
        "seoDescription": "{seoDescription}",
        "slug": "{slug}",
        "title": "{title}"
    }},
    "nbformat": 4,
    "nbformat_minor": 4
}}'''
    return meta_data_template
