//Headers
#include <iostream>
#include <queue>
#include "stdio.h"
//Librarys of opencv 4.5.1
#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace cv;
using namespace std;

Mat BTC(Mat src, int blockSize);

Mat DCT2D_forward(Mat src)
{
	int num_rows = src.rows;
	int num_cols = src.cols;
    
	Mat dst = Mat::zeros(num_rows, num_cols, CV_64F);
	Mat spectrum = Mat::zeros(num_rows, num_cols, CV_8U);

	for (int j = 0; j < num_rows; j++){
		for (int i = 0; i < num_rows; i++){
			double data = 0;
			for (int y = 0; y < num_rows; y++){
				for (int x = 0; x < num_cols; x++){
					double f_xy = (double)src.ptr<uchar>(y)[x];
					data += (double)(f_xy * cos((2.0 * y + 1) * j * CV_PI / 2.0 / num_rows) * cos((2.0 * x + 1) * i * CV_PI / 2.0 / num_rows));
				}
			}
            
			double ci, cj = 0;
			ci = (i == 0) ? (1 / sqrt(2.0)) : 1.0;
			cj = (j == 0) ? (1 / sqrt(2.0)) : 1.0;

			data *= (2.0 / num_rows) * ci * cj;
			dst.ptr<double>(j)[i] = data;
		}
	}
	dst.convertTo(spectrum, CV_8U);
	imshow("Freq_spectrum", spectrum);
	imwrite("Freq_spectrum.bmp", spectrum);
	return dst;
}

Mat DCT2D_inverse(Mat src)
{
    int num_rows = src.rows;
    int num_cols = src.cols;
    
	Mat dst = Mat::zeros(num_rows, num_cols, CV_64F);
	Mat spatial = Mat::zeros(num_rows, num_cols, CV_8U);

	for (int y = 0; y < num_rows; y++){
		for (int x = 0; x < num_cols; x++){
			double data = 0;
			for (int j = 0; j < num_rows; j++){
				for (int i = 0; i < num_rows; i++){
					double F_ij = src.ptr<double>(j)[i];
					double ci = (i == 0) ? (1 / sqrt(2.0)) : 1.0;
					double cj = (j == 0) ? (1 / sqrt(2.0)) : 1.0;
					data += (double)(ci * cj * F_ij * cos((2.0 * y + 1) * j * CV_PI / 2.0 / num_rows) * cos((2.0 * x + 1) * i * CV_PI / 2.0 / num_rows));
				}
			}
			data *= (2.0 / num_rows);
			dst.ptr<double>(y)[x] = data;
		}
	}
    
	dst.convertTo(spatial, CV_8U);
	imshow("Spatial", spatial);
	imwrite("Spatial.bmp", spatial);
	return dst;
}

Mat BTC(Mat src, int blockSize)
{
	int num_rows = src.rows;
	int num_cols = src.cols;
	Mat tmp = Mat::zeros(Size(num_rows, num_cols), CV_32F);
	Mat dst = Mat::zeros(Size(num_rows, num_cols), CV_8U);
	
	for (int i = 0; i < num_rows; i += blockSize){
		for (int j = 0; j < num_cols; j += blockSize){
			float first_moment = 0, second_moment = 0;
			for (int m = 0; m < blockSize; m++){
				for (int n = 0; n < blockSize; n++){
					first_moment += (float)src.ptr<uchar>(i + m)[j + n];
					second_moment += (float)src.ptr<uchar>(i + m)[j + n] * src.ptr<uchar>(i + m)[j + n];
				}
			}
			float blockMean = first_moment / blockSize / blockSize * 1.0;
			float blockVar = sqrt((second_moment / blockSize / blockSize * 1.0) - blockMean * blockMean);

			int n_plus = 0, n_minus = 0;
			for (int m = 0; m < blockSize; m++){
				for (int n = 0; n < blockSize; n++){
					int tmpValue = src.ptr<uchar>(i + m)[j + n];
					if (tmpValue < blockMean)
						n_minus += 1;
					else if (tmpValue >= blockMean){
						n_plus += 1;
					}
				}
			}

			float x_minus = blockMean - blockVar * sqrt(1.0 * n_plus / n_minus);
			float x_plus = blockMean + blockVar * sqrt(1.0 * n_minus / n_plus);

			for (int m = 0; m < blockSize; m++){
				for (int n = 0; n < blockSize; n++){
					int tmpValue = src.ptr<uchar>(i + m)[j + n];
					if (tmpValue < blockMean)
						tmp.ptr<float>(i + m)[j + n] = x_minus;
					else if (tmpValue >= blockMean){
						tmp.ptr<float>(i + m)[j + n] = x_plus;
					}
				}

			}
		}
	}

	tmp.convertTo(dst, CV_8U);
    imshow("DCT", dst);
    imwrite("DCT.bmp", dst);
	return dst;
}

int main()
{
    Mat src = imread("lena.bmp", 0);
    resize(src, src, Size(256, 256));
    
    Mat DCT_freq = DCT2D_forward(src);
    Mat DCT_spat = DCT2D_inverse(DCT_freq);
    
    Mat btcf = BTC(src, 4);
    waitKey(0);
    
    return 0;
}
