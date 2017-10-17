import { Component, OnInit } from '@angular/core';
import { MatToolbar, MatGridList, MatGridTile } from '@angular/material'; 
import { RecpCardComponent } from './recp-card/recp-card.component';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  cards: RecpCardComponent[] = [];
  rec_cards: RecpCardComponent[] = [];

  label: string;
  ingredientLines: string [];
  healthLabels: string [];
  dietLabels: string[];
  url: string;
  image: string;
  calories: number;

  rec_label: string;
  rec_ingredientLines: string [];
  rec_healthLabels: string [];
  rec_dietLabels: string[];
  rec_url: string;
  rec_image: string;
  rec_calories: number;
  



  constructor(private http: HttpClient){
  
  }

  
  ngOnInit(): void {  
    this.http.get('https://1094eb34.ngrok.io/getUserChoices').subscribe(data => {
      for (var i = 0; i < Object.keys(data).length; i++) {  
        this.label = data[i].recipe.label;
        this.ingredientLines = data[i].recipe.ingredientLines;
        this.healthLabels = data[i].recipe.healthLabels;
        this.dietLabels = data[i].recipe.dietLabels;
        this.url = data[i].recipe.url;
        this.image = data[i].recipe.image;
        this.calories = data[i].recipe.calories;

        var addCard = new RecpCardComponent(this.label, this.ingredientLines, this.healthLabels, this.dietLabels, this.url, this.image, this.calories);
        this.cards.push(addCard);
      }
    });
    
    this.http.get('https://1094eb34.ngrok.io/randomRecipe').subscribe(data => {
      console.log(data['recipe'].url);
      for (var i = 0; i < Object.keys(data).length; i++) {  
        this.rec_label = data['recipe'].label;
        this.rec_ingredientLines = data['recipe'].ingredientLines;
        this.rec_healthLabels = data['recipe'].healthLabels;
        this.rec_dietLabels = data['recipe'].dietLabels;
        this.rec_url = data['recipe'].url;
        this.rec_image = data['recipe'].image;
        this.rec_calories = data['recipe'].calories;

        var addCard = new RecpCardComponent(this.rec_label, this.rec_ingredientLines, this.rec_healthLabels, this.rec_dietLabels, this.rec_url, this.rec_image, this.rec_calories);
        this.rec_cards.push(addCard);
      }
    });  
  }
}
