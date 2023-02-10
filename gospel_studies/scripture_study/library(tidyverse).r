library(tidyverse)

html <- read_html("https://rvest.tidyverse.org/")

sections <- html_elements("div")

sections |> 
    html_element("h2") |>
    html_text2()






scriptures_df <- data.frame()

baseURL <- "https://www.churchofjesuschrist.org/study/scriptures/"

"https://www.churchofjesuschrist.org/study/scriptures/pgp/abr/3?lang=eng"

standard_work <- list("ot", "nt", "bofm", "dc-testament", "pgp")
book <- ""
chapter <- ""

loopURL <- paste0()

for (i in seq(1, 13, 2)){
    print(i)
}

str_glue("Hey {standard_work[[1]]}")

library(scriptuRs)
lds_scriptures() |> 
    mutate(
        locations = NA, 
        geography = NA,
        individuals = NA, 
        groups_of_people = NA, 
        number_of_references_to_Savior = NA, 
        references_to_Savior = NA, #dictionary? nested?
        doctrinal_concepts = NA, 
        priesthood_lineage_in_play = NA, 
        speakers = NA, 
        writers = NA, 
        Mormon_commentary = NA, 
        Moroni_commentary = NA, 
        plates_origin = NA, #what set of plates this came from 
        whowouldhavehadaccesstothisbookinthepast = NA, #list of individuals/groups of people
    ) |> 
    filter(book_title == "John") |> 
    # select(locations, individuals, verse_title, text) |> 
    head() |> 
    knitr::kable()



# https://jtr13.github.io/cc19/web-scraping-using-rvest.html
# https://rvest.tidyverse.org/
# https://rvest.tidyverse.org/reference/index.html
# https://glue.tidyverse.org/
# https://cran.r-project.org/web/packages/scriptuRs/scriptuRs.pdf
# https://github.com/andrewheiss/scriptuRs
# https://github.com/beandog/lds-scriptures
# https://scriptures.nephi.org/




'//*[contains(concat( " ", @class, " " ), concat( " ", "style__navLogoImage_zBWSx", " " ))]'

