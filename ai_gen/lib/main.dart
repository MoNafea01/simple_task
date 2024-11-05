import 'package:ai_gen/sonnet_code.dart';
import 'package:flutter/material.dart';

import 'block_view/example.dart';

void main() async {
  print(await trainTestSplit([1, 2, 3, 4], testSize: 0.2, randomState: 1));
  runApp(const MyApp());
}

TextEditingController controller = TextEditingController();

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Test Demo',
      theme: ThemeData(
        scaffoldBackgroundColor: const Color.fromARGB(255, 46, 46, 46),
      ),
      home: const VSNodeExample(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});
  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String? output;

  void _incrementCounter() async {
    try {
      // Get the input text from the controller and parse it as a list
      List<double> data = controller.text
          .split(',') // Split the string by commas
          .map((e) => double.parse(e.trim())) // Parse each element to a double
          .toList();

      print('Parsed data: $data');

      output = "Loading ...";

      // Call your trainTestSplit method with the parsed data
      final result = await trainTestSplit(data, testSize: 0.3, randomState: 42);

      // Display the result
      output =
          'Training set: ${result['X_train']}\nTest set: ${result['X_test']}';

      print('Training set: ${result['X_train']}');
      print('Test set: ${result['X_test']}');
    } catch (e) {
      // If there is an error (e.g., invalid input format), show an error message
      output =
          'Error: Invalid input format. Please enter comma-separated numbers.';
      print('Error: $e');
    }

    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appBar(context),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Padding(
              padding: EdgeInsets.all(10),
              child: CustomTextField(),
            ),
            Text(
              '$output',
              style: Theme.of(context).textTheme.bodyMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Train',
        child: const Icon(Icons.refresh),
      ),
    );
  }

  AppBar appBar(BuildContext context) {
    return AppBar(
      backgroundColor: Theme.of(context).colorScheme.inversePrimary,
      title: const Text("Demo"),
    );
  }
}

class CustomTextField extends StatelessWidget {
  const CustomTextField({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: controller,
      decoration: InputDecoration(
        label: const Text('array of Data'),
        suffixIcon: IconButton(
          onPressed: () {
            controller.clear();
          },
          icon: Icon(Icons.clear, color: Colors.grey[600]),
        ),
        contentPadding:
            const EdgeInsets.symmetric(vertical: 18.0, horizontal: 20.0),
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(30.0),
          borderSide: const BorderSide(color: Colors.black),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(30.0),
          borderSide: const BorderSide(color: Colors.blueAccent),
        ),
      ),
      style: const TextStyle(color: Colors.black87, fontSize: 16.0),
    );
  }
}
