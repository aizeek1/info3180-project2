app.controller('WishlistController', ['$scope','$http','$location', function($scope,$http,$location){
	if(localStorage.userID == null){
		$location.url("/")
	}

	config = {

			headers:{'Accept': "json",
			"Authorization":"Basic " +localStorage.token

			}
	}

	$http.get('/api/users/'+localStorage.userID+'/wishlist', config).then(function(response){
		
			if(response.data.message =="Success"){
				$scope.wishlist = response.data.data.items
			}
			
	
	})
}])