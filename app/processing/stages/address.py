# # from app.processing.stages.ocr import run_ocr


# def extract_address(text: str) -> str | None:
#     lines = [line.strip() for line in text.splitlines()]

#     START_MARKERS = {
#     "DELIVER TO",
#     "SHIP TO",
#     "BILL TO",
# }

#     for i, line in enumerate(lines):
#         if line.upper() == "DELIVER TO":
#             start = i + 1
#             break

#     if START_MARKERS is None:
#         return None

#     STOP_WORDS = {
#         "CONTACT",
#         "INVOICE DATE",
#         "ORDER NO",
#         "CLERK",
#         "PAYMENT DUE BY",
#         "CON NOTE",
#         "CARRIER",
#         "ITEM CODE",
#     }

#     address = []

#     for line in lines[start:]:
#         if line.upper() in STOP_WORDS:
#             break

#         if line:
#             address.append(line)

#     return "\n".join(address)