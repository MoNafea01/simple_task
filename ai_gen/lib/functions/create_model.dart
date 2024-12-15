import 'package:ai_gen/classes/model_class.dart';
import 'package:dio/dio.dart';

Future<AIModel> createModel(Map<String, dynamic> modelData) async {
  final dio = Dio();

  var data = {
    "model_name": modelData['model_name'],
    "params": modelData['params'],
    "model_type": modelData['model_type'],
    "task": modelData['task'],
  };

  print(data);
  try {
    final response = await dio.post(
      'http://127.0.0.1:8000/create_model/',
      data: data,
      options: Options(contentType: Headers.jsonContentType),
    );

    if (response.statusCode == 200 || response.statusCode == 201) {
      final jsonResponse = response.data;
      final model = AIModel.fromJson(jsonResponse);
      print("model: ${model.toJson()}");
      return model;
    } else {
      throw Exception('Failed to perform createModel');
    }
  } on DioException catch (e) {
    // Handle Dio-specific exceptions
    if (e.response != null) {
      throw Exception(
          'Failed to perform createModel: ${e.response?.statusCode}');
    } else {
      throw Exception('Network error: ${e.message}');
    }
  }
}
