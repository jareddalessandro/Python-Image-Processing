# Python Image Processing
## Basic example script showing how to manipulate an image at the pixel level using python. 

## Before
![road](https://user-images.githubusercontent.com/13529116/93648179-fce21980-f9be-11ea-8915-59fa0e8cb0e5.jpg)

## After
![road_basicLighten](https://user-images.githubusercontent.com/13529116/93648190-08354500-f9bf-11ea-8570-945a444e3b77.jpg)

## TroubleShooting:
- Image is being rotated unexpectedly: If you use images taken by a mobile phone the image likely contains metadata directing the phone to rotate the image so the image is displayed correctly on the phone. This metadata is not taken into consideration by this application and the rendered image will be displayed as if being rotated compared to the original.