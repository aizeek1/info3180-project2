// Your JavaScript Code here
/* global angular */


var imageapp = angular.module('myApp', []);
imageapp.controller('myImage', function($scope, $http) {
   $http.get("/api/thumbnails").then(function (response) {
       console.log(response.data.thumbnails);
      $scope.myThumbnails =response.data.thumbnails;
   });
      
   // $http.get('/api/home', {
   //    headers: {
   //       'Content-type': 'application/json'
   //    }
   // });
   
   $scope.get_pics = function(event) {

      event.preventDefault();

      $http.get('/api/thumbnails?image_url=' +$scope.image_url).success(function (response) {


         console.log(response.thumbnails.length);
         
         $scope.thumbs = response.thumbnails;
      }).
      error(function (error) {
         console.log(error)
      });
   
   }
});

// var app  = angular.module('myApp2', ['ngRoute']);

// app.config(['$routeProvider',function($routeProvider, $locationProvider){

// 	$routeProvider
// 	.when('/',{
// 		templateUrl:'/templates/home.html'
// 	})
// 	.when('/wishlist',{
// 		controller:'WishlistCtrl',
// 		templateUrl:'/templates/wishlist.html'
// 	})
// 	.otherwise({
// 		redirectTo:'/'
// 	})


// }])

//var request = new XMLHttpRequest();
//request.setRequestHeader("Content-Type","text/plain");
// request.setRequestHeader("Authorization", "Basic " + ("username:password"));

// $http.get('https://www.example.com/someapi', {
//  headers: {
//  'Content-Type': 'application/json'
//  }
// });