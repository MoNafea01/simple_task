import 'package:dio/dio.dart';

Future<Map<String, List<double>>> trainTestSplit(
  List<double> data, {
  double testSize = 0.2,
  int? randomState,
}) async {
  final dio = Dio();

  try {
    final response = await dio.post(
      'http://127.0.0.1:8000/ai/train-test-split/',
      data: {
        'data': data,
        'test_size': testSize,
        'random_state': randomState,
      },
      options: Options(
        contentType: Headers.jsonContentType,
      ),
    );

    if (response.statusCode == 200) {
      final jsonResponse = response.data;
      return {
        'X_train': List<double>.from(jsonResponse['X_train']),
        'X_test': List<double>.from(jsonResponse['X_test']),
      };
    } else {
      throw Exception('Failed to perform train-test split');
    }
  } on DioException catch (e) {
    // Handle Dio-specific exceptions
    if (e.response != null) {
      throw Exception(
          'Failed to perform train-test split: ${e.response?.statusCode}');
    } else {
      throw Exception('Network error: ${e.message}');
    }
  }
}
