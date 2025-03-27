library(tidyverse)
library(tibble)
library(readr)
library(dplyr)
library(magrittr)
library(ggplot2)
nettle <- read.csv('nettle_1999_climate.csv')
nettle <- as_tibble(nettle)
nettle
nettle <- read_csv('nettle_1999_climate.csv')
nettle
filter(nettle, Country ==  'Nepal')
select(nettle, Langs, Country)
select(nettle, Area:Langs)
nettle <- rename(nettle, Pop = Population)
nettle
nettle <- mutate(nettle, Lang100 = Langs / 100)
nettle
arrange(nettle, Langs)
arrange(nettle, desc(Langs))
ggplot(nettle)+
  geom_point(mapping = aes (x = MGS, y = Langs))
ggplot(nettle, aes(x = MGS, y = Langs, label = Country))+
  geom_text()
ggsave('nettle.png', width = 8, height = 6)

nettle %>%
  filter(MGS > 8) %>%
  ggplot(aes(x=MGS, y=Langs, label = Country))+
  geom_text()





1960*(6.1+0.53)/(26.28-6.1)

nettletwo <- read.csv('SuppPub1.csv')
nettletwo
class(nettletwo$F2)


non_numeric <- !grepl("^[0-9.]+$", nettletwo$F1)
print(data[non_numeric])



mean(nettle$F1)
class(nettle$F1)
nettle$F1 <- as.numeric(nettle$F1)
class(nettle$F1)
nettle$F1




p <- rnorm(50)
head(p)
y <- 10+3*p
plot(p, y, pch=19)
error<- rnorm(50)
y <- 10+3*p+error
plot(p, y, pch=19)
xmdl <- lm(y ~ p)
xmdl
head(fitted(xmdl))
head(residuals(xmdl))

