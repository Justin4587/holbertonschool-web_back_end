youveGotMail = re.sub(f"(?<={target}=).*?(?={separator})", redaction, message)