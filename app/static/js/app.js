// Your JavaScript Code here
/* global angular */


var imageapp = angular.module('myApp', []);
imageapp.controller('myImage', function($scope, $http) {
   $http.get("/api/thumbnails").then(function (response) {
       console.log(response.data.thumbnails);
      $scope.myThumbnails =response.data.thumbnails;
   });
   
   $scope.get_pics = function(event) {

      event.preventDefault();

      $http.post('/process',{'text':$scope.image_url}).success(function (response) {


         console.log(response.thumbnails.length);
         /*var pics_html = [];
         for (i = 0; i < response.thumbnails.length; i++)
         {
            pics_html.push(response.thumbnails[i]);
         }
         console.log(pics_html);*/
         $scope.thumbs = response.thumbnails;
      }).
      error(function (error) {
         console.log(error)
      });
   
   }
});
