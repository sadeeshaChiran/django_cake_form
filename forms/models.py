from django.db import models

# Create your models here.
class Form(models.Model):
    
    # Name
    name = models.CharField(max_length=256)

    #Contact number
    contact_number = models.IntegerField()
    
    #Email
    email = models.EmailField()
    
    #Delivery address
    delivery_address = models.CharField(max_length=256)

    # Occasion 
    OCCASION = [
        ('', 'Select an occasion'),
        ('Birthday', 'Birthday'),
        ('Wedding', 'Wedding'),
        ('Graduation', 'Graduation'),
        ('Baby Shower', 'Baby Shower'),
        ('other', 'Other'),
    ]
    occasion = models.CharField(max_length=100, choices=OCCASION)
    other_occasion = models.CharField(max_length=100, blank=True, null=True)

    
    
    # Cake size
    CAKE_SIZE_CHOICES = [
        ('', 'Select a size'),
        ('6-inch (serves 8-10)', '6-inch (serves 8-10)'),
        ('8-inch (serves 12-15)', '8-inch (serves 12-15)'),
        ('10-inch (serves 20-25)', '10-inch (serves 20-25)'),
        ('Custom size', 'Custom size'),
    ]
    cake_size = models.CharField(max_length=100, choices=CAKE_SIZE_CHOICES)
    other_cake_size = models.CharField(max_length=100, blank=True, null=True)
    
    
    
    # Shape size
    CAKE_SHAPE = [
        ('', 'Select a shape'),
        ('Round', 'Round'),
        ('Square', 'Square'),
        ('Rectangle', 'Rectangle'),
        ('Heart', 'Heart'),
        ('Custom shape', 'Custom shape'),
    ]
    cake_shape = models.CharField(max_length=100, choices=CAKE_SHAPE)
    cake_other_shape = models.CharField(max_length=100, blank=True, null=True)




    # Cake Flavors
    CAKE_FLAVORS = [
        ('', 'Select flavors'),
        ('Buttercream', 'Vanilla'),
        ('Chocolate', 'Chocolate'),
        ('Red Velvet', 'Red Velvet'),
        ('Carrot', 'Carrot'),
        ('Marble', 'Marble'),
        ('Custom flavor', 'Custom flavor'),
    ]
    cake_flavors = models.CharField(max_length=100, choices=CAKE_FLAVORS)
    cake_other_flavors = models.CharField(max_length=100, blank=True, null=True)



    # Cake Filling
    CAKE_FILLING = [
        ('', 'Select a Filling Type'),
        ('Buttercream', 'Buttercream'),
        ('Chocolate Ganache', 'Chocolate Ganache'),
        ('Fruit', 'Fruit'),
        ('Cream Cheese', 'Cream Cheese'),
        ('Custard', 'Custard'),
        ('other', 'Other'),
    ]
    cake_filling = models.CharField(max_length=100, choices=CAKE_FILLING)
    cake_other_filling = models.CharField(max_length=100, blank=True, null=True)
    fruit_types = models.CharField(max_length=100, blank=True, null=True)



    # Cake Frosting
    CAKE_FROSTING = [
        ('', 'Select a frosting'),
        ('Buttercream', 'Buttercream'),
        ('Fondant', 'Fondant'),
        ('Whipped Cream', 'Whipped Cream'),
        ('Chocolate', 'Chocolate'),
        ('Cream Cheese', 'Cream Cheese'),
        ('Naked (Minimal frosting)', 'Naked (Minimal frosting)'),

    ]
    cake_frosting = models.CharField(max_length=100, choices=CAKE_FROSTING)





    # Cake Decorations
    CAKE_DECORATIONS = [
        ('', 'Select a disoration'),
        ('Sprinkles', 'Sprinkles'),
        ('Edible Flowers', 'Edible Flowers'),
        ('Fondant Figures', 'Fondant Figures'),
        ('Chocolate Shavings', 'Chocolate Shavings'),
        ('Fresh Fruits', 'Fresh Fruits'),
        ('Edible Glitter', 'Edible Glitter'),
        ('Custom decoration', 'Custom decoration'),
    ]
    cake_decorations = models.CharField(max_length=100, choices=CAKE_DECORATIONS)
    cake_other_decorations = models.CharField(max_length=100, blank=True, null=True)



    # Cake Text
    text = models.CharField(max_length=256)
    
    # Cake Font Style
    font_style = models.CharField(max_length=256)
    
    # Cake Color
    colour = models.CharField(max_length=256)
    
    # Additional reques
    additional_requests = models.TextField()
    
    # Delivaery or pickup
    DELIVAERY_TYPE = [
        ('', 'Select a delivary type'),
        ('Delivery (extra charges may apply)', 'Delivery (extra charges may apply)'),
        ('Pickup', 'Pickup'),
    ]
    delivaery_or_pickme = models.CharField(max_length=100, choices=DELIVAERY_TYPE)
    

    
    # Preferred Date
    preferred_date = models.DateField()
    
    # Preferred Time
    preferred_time = models.TimeField()
    
    # Payment Method
    PAYMENT_METHOD = [
        ('', 'Select a payment method'),
        ('Cash', 'Cash'),
        ('Credit/Debit Card', 'Credit/Debit Card'),
        ('Online Payment (e.g., PayPal)', 'Online Payment (e.g., PayPal)'),
        ('other', 'other'),
    ]
    paymentmethod = models.CharField(max_length=100, choices=PAYMENT_METHOD, blank=True, null=True )
    other_paymentmethod = models.CharField(max_length=100, blank=True, null=True)
    
    
  
    # Sampal image
    image = models.ImageField(upload_to='media')
    


    
    
    timestamp = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name
