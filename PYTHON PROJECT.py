#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  PYTHON PROJECT.py
#  
#  Copyright 2021 Sri lakshmi <Sri lakshmi@LAPTOP-3GPPA1AF>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from imdb import IMDb

import requests
from bs4 import BeautifulSoup
# create an instance of the IMDb class
ia = IMDb()
# search for a person name


while(True):
	person_name=input("enter an actor or a director name to know few of their popular movies and shows!!\n")
	if person_name=='exit':
		break
	else:
		people = ia.search_person(f"{person_name}")
		url=f"https://www.imdb.com/filmosearch/?role=nm{people[0].personID}"
		response=requests.get(url)
		html=response.text

		soup = BeautifulSoup(html,'html.parser')
		movietags = soup.select('h3.lister-item-header')#using mocvie split we can get year and movie name print 5 movie names with yaer director stars rating
		innermovietag=soup.select('h3.lister-item-header a')
		rating_tags=soup.select('div.ratings-bar strong')
		text="lister-item-year text-muted unbold"
		year_tags=soup.find_all('span', {'class' : 'lister-item-year text-muted unbold'})
		num=5
		if len(movietags)<num:
			num=len(movietags)
	
		for index in range(num):
			movie_rating=rating_tags[index].text # u got rating yayyy
			movie_split=movietags[index].text.split()
			year=year_tags[index].text
			movie_name=innermovietag[index].text
			print(f"movie name: {movie_name} {year}\n rating: {movie_rating}")
		print("if you want to end the program type 'exit'")
	    
	
	    
	    
	
	


	
		
	    
	    
	    
	
	
		
	




    


	



   

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
