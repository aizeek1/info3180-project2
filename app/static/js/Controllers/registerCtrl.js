app.controller('RegisterCtrl', ['$scope', '$http','$location', function($scope, $http,$location){
		
	if(localStorage.userID != null){
		$location.url("/")
	}

	$scope.register = function(){

		data = {

			'email':$scope.email,
			'name':$scope.name,
			'password':$scope.password,
			'age':$scope.age,
			'gender':$scope.gender

		}

		config = {

				headers:{'Content-Type': "application/json"}

			}
		
		$http.post('/api/users/register', data, config).then(function(response){
			if(response.data.message == "Success"){
				$location.url('/')
			}
		})


	}
}]);