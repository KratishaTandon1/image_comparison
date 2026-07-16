import pypdf

reader = pypdf.PdfReader(r"c:\Users\prakh\Downloads\Product_Task_July2026.pdf")
for page_num, page in enumerate(reader.pages):
    if "/Annots" in page:
        for annot in page["/Annots"]:
            obj = annot.get_object()
            if obj.get("/Subtype") == "/Link":
                uri = obj.get("/A", {}).get("/URI")
                if uri:
                    print(f"Page {page_num + 1}: {uri}")
