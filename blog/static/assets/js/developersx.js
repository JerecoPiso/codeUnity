
	

	var developers_skills = {
		delimiters: ['[', ']'],
		props:{
			
			skills: String,
			// dev_skills: String	
		},
		data: function(){

			return{
				skill: this.skills,
				dev_skills: String,
			}

		},
		created: function(){
			this.dev_skills = this.getSkills(this.skill)
		
			// alert(this.dev_skills)
		},
		methods:{
			getSkills: function(skill){
				var str = skill
			
				var n = null;
				var skill = ""
				// var num = str.search(",");
				var counter = 0
				while(str.length != 0){
					var ctr = str.search(",");
				
					if(ctr != -1){
						n = str.slice(0,ctr)
						str = str.slice(ctr+1,str.length)
					
						skill = skill+"<a href='/developers/skills/"+n+"' class='skill-link'>"+n+"</a>";
						
					}else{
						str = str.slice(0,str.length)
						skill = skill+"<a href='/developers/skills/"+str+"' class='skill-link'>"+str+"</a>";
					
						str = ""
						
						
					
					}
					counter++;
					if(counter == 9){
						break;
					}
					
				}
			
				return skill
			}
		},
		template: '<div id="" style=" display: flex;flex-wrap: wrap;margin: -5px 5px 5px 0;font-size: 8px" v-html="dev_skills"></div>'
	}
	new Vue({
		delimiters: ['[', ']'],
		el: "#developers",
		data:{
			search: '',
			showRates: false,
			countries: [],
			country: 'Select Country',
			min: Number,
			max: Number,
			devInfo:{flag: '', rate: '', img: '', name: '', expertise: '', skills: '', photo: '', aboutme: '', resume: ''},
			media: '/media/',
		
		
		},
		components:{
			"dev-skills": developers_skills
		},
		mounted: function(){
			for(var i = 0; i < countryList.length; i++){
				this.countries.push({
					name: countryList[i].name,
					countryAbbr: countryList[i].code.toLowerCase()
				})
			}
		},
		methods:{
			showDev: function(flag,rate,expertise,skills,photo,name,aboutme, resume){
				
				var str = skills
			
				var n = null;
				var skill = ""
				// var num = str.search(",");
				var counter = 0
				while(str.length != 0){
					var ctr = str.search(",");
				
					if(ctr != -1){
						n = str.slice(0,ctr)
						str = str.slice(ctr+1,str.length)
					
						skill = skill+"<a href='javascript:void(0)' class='skill-link'>"+n+"</a>";
						
					}else{
						str = str.slice(0,str.length)
						skill = skill+"<a href='javascript:void(0)' class='skill-link'>"+str+"</a>";
					
						str = ""
						
						
					
					}
					counter++;
					if(counter == 9){
						break;
					}
					
				}
				
				this.devInfo.skills = skill
				this.devInfo.flag = flag
				this.devInfo.photo = photo
				this.devInfo.expertise = expertise
				this.devInfo.rate = rate
				this.devInfo.name = name
				this.devInfo.aboutme = aboutme
				this.devInfo.resume  = resume
				$(".modalDeveloper").fadeToggle()
			},
			hideDev: function(){
				$(".modalDeveloper").fadeToggle()
			},
			searchRate: function(){
				window.location.href="/developers/rate/"+Number(this.min)+"/"+Number(this.max)
			},
			showClose: function(){
				if(this.showRates === false){
					$(".set-rate").slideToggle()
					this.showRates = true
				}else{
					$(".set-rate").slideToggle()
					this.showRates = false
				}
			},
			searchCountry: function(){
				window.location.href="/developers/country/"+this.country
			},
			searchDevs: function(){
				
				window.location.href="/developers/search/"+this.search
			}
		}
	})
	
	




 
