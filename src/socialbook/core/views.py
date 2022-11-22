from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile,Post,LikePost
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url = 'signin')
def home (request):

    
    profile_prev =  Profile.objects.get(user=request.user)
    post_feed = Post.objects.all()
    context= {
        'profile_prev' : profile_prev,
        'posts': post_feed,
    }

   
    return render(request,'index.html',context)

def upload(request):
  if request.method =='POST':
        user = request.user.username
        image = request.FILES.get('image')
        caption = request.POST.get('caption') 

        post_feed = Post.objects.create(user=user , image =image , caption = caption )
        post_feed.save()

        return redirect('/')
  else:
    return render (request,'index.html')
    

def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id= post_id)

    like_filter = LikePost.objects.filter(post_id=post_id , username = username).first()
    if like_filter==None:
        new_like = LikePost.objects.create(post_id= post_id , username=username)
        new_like.save()
        post.no_likes = post.no_likes + 1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_likes = post.no_likes-1
        post.save()
        return redirect('/')




    

    



def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password==password2:
           
           if User.objects.filter(username=username).exists():
               messages.info(request ,'Username already exists. Try another one ' )
               return redirect('signup')
           elif User.objects.filter(email=email).exists():
               messages.info(request, 'Email already used. Try another one')
               return redirect('signup')
           else:
                user = User.objects.create_user(username=username,email=email,password=password)  
                user.save()
                
             # log in the user

             # create a profile object for the new user
                user_model = User.objects.get(username=username)
                profile_model = Profile.objects.create(user = user_model , id_user=user_model.id)
                profile_model.save()  
                user = auth.authenticate(username=username,password=password)
                auth.login(request,user)
                return redirect('settings')

        else:
            messages.info(request,'Password does not match. Try again')
            return redirect('signup')
    else:
         return render(request,'signup.html')



def signin (request):
    if request.method == 'POST':
        # taking the inputs 
        username = request.POST.get('username')
        password= request.POST.get('password')
        
        # now authenticating the user

        user = auth.authenticate(username=username,password=password)

        if user is not None:
             auth.login(request,user)
             return redirect('/')
        else:
            messages.info(request,'Invalid credentials. Check the username and password again')
            return redirect('signin')
    else:
       return render(request,'signin.html')

def logout(request):

    auth.logout(request)
    return redirect('signin')




def settings(request):
    profile_model = Profile.objects.get(user=request.user)
    context = {
       'profile_model' : profile_model,
    }

    if request.method=='POST':
        if request.FILES.get('image')==None:
            image = profile_model.profile_img
            bio = request.POST.get('bio')
            location = request.POST.get('location')

            profile_model.profile_img = image
            profile_model.bio = bio
            profile_model.location = location
            profile_model.save()
        if request.FILES.get('image') != None:
            image =  request.FILES.get('image')
            bio = request.POST.get('bio')
            location = request.POST.get('location')

            profile_model.profile_img = image
            profile_model.bio = bio
            profile_model.location = location
            profile_model.save()
        return redirect('settings')
    else:
       return render(request,'setting.html',context)


def profile(request):
    return render(request,'profile.html')