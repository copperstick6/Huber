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

  label: string;
  ingredientLines: string [];
  healthLabels: string [];
  dietLabels: string[];
  url: string;
  image: string;
  calories: number;


  constructor(private http: HttpClient){
  
  }

  
  ngOnInit(): void {
    this.http.get('http://1094eb34.ngrok.io/getUserChoices').subscribe(data => {
      console.log(data[0]);
      var temp = JSON.stringify(data[0].recipe);
      console.log(data[0].recipe.calories);
      console.log(data[0].recipe.image);
      console.log((Object.keys(data).length));

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
  }
}
