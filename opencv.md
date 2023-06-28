### Data Types

* CV_8U - 8 bit unsigned integer
* CV_8S - 8 bit signed integer
* CV_16U - 16 bit unsigned integer
* CV_16S - 16 bit signed integer
* CV_32S - 32 bit signed integer
* CV_32F - 32 bit floating point number
* CV_64F - 64 bit float floating point number

### Mat - iamge container


####  creating a blank image

many constructors are available in Mat class.Below when 3 channel image is created 8*3 bits are allocated to each pixel 

-  Mat image(600, 800, CV_8UC3, Scalar(100, 250, 30));

#### zeros and ones and eye
```cpp
Mat E = Mat::eye(4, 4, CV_64F);
Mat O = Mat::ones(4, 4, CV_8S);
Mat Z = Mat::zeros(2, 2, CV_32F);
```

#### clone rows
```cpp
Mat row = image.row(0).clone();
cout << row << endl;
```

#### fill random values
```cpp
Mat rand = Mat(4, 4, CV_8SC1);
randu(rand, Scalar::all(0), Scalar::all(200));
cout << rand << endl;
```

#### accessing pixel values 
##### meth 1
```cpp
struct rgb {
    uchar blue;
    uchar green;
    uchar red;
};

for (int i = 0;i < image.rows;i++) {
      for (int j = 0;j < image.cols;j++) {
          cout << (int)image.at<uchar>(i, j) << " ";
           
          rgb& color = image.ptr<rgb>(i)[j];

          cout << (int)color.blue << " " ;
          cout << (int)color.green << " ";
          cout << (int)color.red << " ";
          

          Vec3b& bgr = image.at<Vec3b>(i, j);
          cout << bgr[0] << " " << bgr[1] << " " << bgr[2] << " ";
      }
      cout << endl;
  }
```
##### meth 2
```cpp
uint8_t* pixelptr = (uint8_t *)image.data;
int chan = image.channels();
Scalar_<uint8_t> bgrpixel;

for (int i = 0;i < image.rows;i++) {
    for (int j = 0;j < image.cols;j++) {
        bgrpixel.val[0] = pixelptr[i * image.cols * chan + j * chan + 0];
        bgrpixel.val[1] = pixelptr[i * image.cols * chan + j * chan + 1];
        bgrpixel.val[2] = pixelptr[i * image.cols * chan + j * chan + 2];
        cout << bgrpixel.val[0] << " ";
        cout << bgrpixel.val[1] << " ";
        cout << bgrpixel.val[2] << " ";
    }
    cout << endl;
}
```

#### print all pixels values in 1D continuous image
```cpp
Mat rand = Mat(4, 4, CV_8SC3);
randu(rand, Scalar::all(0), Scalar::all(200));
cout << rand << endl;

int chan = rand.channels();
int nrows = rand.rows;
int ncols = rand.cols*chan;


if (rand.isContinuous()) {
    ncols = ncols * nrows;
    nrows = 1;
}

for (int i = 0;i < nrows;i++) {
    uchar* p = rand.ptr<uchar>(i);
    for (int j = 0;j < ncols;j++) {
        cout << (int)p[j] << " ";
    }
}
```

#### Devide rgb values into seperate images


#### select ROI 

```cpp

```
