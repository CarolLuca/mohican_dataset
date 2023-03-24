from images_google import get_google_img

def clean_company(company):
    cleaned_company = company.strip(" ")
    return cleaned_company

def clean_motto(motto):
    pc_motto = motto.strip(" ")

    cleaned_motto = ""
    for word in pc_motto.split(" "):
        if word.startswith("(") == False and word.endswith(")") == False:
            cleaned_motto += word + " "

    cleaned_motto = cleaned_motto[:len(cleaned_motto)-1]
    return cleaned_motto

def clean_csv(input_file, output_file):
    inf = open(input_file, "r", errors = "ignore")
    outf = open(output_file, "w")

    lines = inf.readlines()
    for line in lines:
        company = line.split(",")[0]
        motto = line.split(",")[1]

        company = clean_company(company)
        motto = clean_motto(motto)

        outf.write(company + "," + motto)

    inf.close()
    outf.close()

def create_dataset(input_file, output_file):
    inf = open(input_file, "r", errors = "ignore")
    outf = open(output_file, "w")

    lines = inf.readlines()
    for line in lines:
        company = line.split(",")[0]
        motto = line.split(",")[1]

        logo = get_google_img(company + " logo")
        ad = get_google_img(company + " \"ad\"")

        outf.write(company + "," + logo + "," + ad + "," + motto)

    inf.close()
    outf.close()

if __name__ == '__main__':
    clean_csv("dirty_name_motto.csv", "cleaned_name_motto.csv")
    create_dataset("cleaned_name_motto.csv", "name_logo_ad_motto.csv")
