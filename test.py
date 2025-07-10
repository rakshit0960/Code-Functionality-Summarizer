class DataProcessor:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.data = []
        
    def load_data(self):
        """Loads data from the input file into memory"""
        try:
            with open(self.input_file, 'r') as f:
                self.data = [line.strip() for line in f]
        except FileNotFoundError:
            print(f"Error: File {self.input_file} not found")
            return False
        return True

    def process_data(self):
        """Processes the loaded data by:
        1. Converting to uppercase
        2. Removing duplicates 
        3. Sorting alphabetically
        """
        if not self.data:
            return []
            
        processed = [item.upper() for item in self.data]
        processed = list(set(processed))
        return sorted(processed)
        
    def save_results(self, output_file: str):
        """Saves processed results to output file"""
        processed_data = self.process_data()
        try:
            with open(output_file, 'w') as f:
                for item in processed_data:
                    f.write(f"{item}\n")
            return True
        except Exception as e:
            print(f"Error saving results: {e}")
            return False


class DataValidator:
    def __init__(self):
        self.validation_rules = []
        
    def add_rule(self, rule_func):
        """Adds a validation rule function"""
        self.validation_rules.append(rule_func)
        
    def validate(self, data):
        """Validates data against all rules"""
        results = []
        for rule in self.validation_rules:
            results.append(rule(data))
        return all(results)


class DataTransformer:
    @staticmethod
    def to_uppercase(data):
        """Converts all strings in data to uppercase"""
        return [str(item).upper() for item in data]
        
    @staticmethod
    def remove_duplicates(data):
        """Removes duplicate entries from data"""
        return list(set(data))
        
    @staticmethod
    def sort_alphabetically(data):
        """Sorts data alphabetically"""
        return sorted(data)


def main():
    # Example usage
    processor = DataProcessor("input.txt")
    validator = DataValidator()
    transformer = DataTransformer()
    
    # Add validation rules
    validator.add_rule(lambda x: len(x) > 0)  # Check if data is not empty
    
    if processor.load_data():
        data = processor.data
        if validator.validate(data):
            processor.save_results("output.txt")
            print("Processing complete!")
        else:
            print("Data validation failed")
    else:
        print("Failed to process data")

if __name__ == "__main__":
    main()
