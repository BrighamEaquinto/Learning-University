library(tidyverse)
library(rvest)
library(purr)

url <- "https://en.wikipedia.org/wiki/Web_scraping"

source <- read_html(url)

(h2_headers <- source |>
    html_elements("h2") |>
    html_text2())


url1 <- "https://en.wikipedia.org/wiki/Special:Random"


myfunc <- function(url1) {

read_html(url1) %>% 
    html_elements("h1") %>% 
    html_text2()

}

purrr::map(rep(url1, 20), ~myfunc(.x))

#### How many links in wiki article?

url2 <- "https://en.wikipedia.org/wiki/Brigham_Young_University%E2%80%93Idaho"

read_html(url2) %>% 
    html_elements("#bodyContent") %>% 
    html_elements('a') %>% 
    html_text() %>% 
    length()

#### Simsons Scripts

url3 <- "https://simpsons.fandom.com/wiki/Category:Transcripts"

url_transcripts <- paste0(read_html(url3) %>% 
    html_elements(".category-page__member-link") %>% 
    html_attr("href"))

