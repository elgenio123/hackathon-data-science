from flask import Flask, request, jsonify
from helpers import concatenate_lists, get_male_first_names, get_female_first_names, get_last_names, get_commune_names, generate_students_names

app = Flask(__name__)

@app.route('/boys', methods=['GET'])
def get_boys_names():
    try:

        if not all([]):
            return jsonify({'error': 'Missing parameters'}), 400
        
        url = 'https://top-names.info/names.php?S=M&P=CAM'
        s = get_male_first_names(url)

        return jsonify({'data': str(s), "length": len(s)})

    except Exception as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 400

@app.route('/girls', methods=['GET'])
def get_girls_names():
    try:
        event_flag = request.args.get('event_flag')

        if not all([]):
            return jsonify({'error': 'Missing parameters'}), 400
        
        url = 'https://top-names.info/names.php?S=F&P=CAM'
        s = get_female_first_names(url)

        return jsonify({'data': str(s), "length": len(s)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/last-names', methods=['GET'])
def get_last_name():
    try:
        
        url = "./last_names.html"
        s = get_last_names(url)

        return jsonify({'data': str(s), "length": len(s)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/commune-names', methods=['GET'])
def get_commune():
    try:
        url = 'https://en.m.wikipedia.org/wiki/Communes_of_Cameroon'
        s = get_commune_names(url)

        return jsonify({'data': str(s), "length": len(s)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/generate-last-names', methods=['GET'])
def generate_last_names():
    try:
        size = request.args.get('size')
        seed = request.args.get('seed')

        if not all([size, seed]):
            return jsonify({'error': 'Missing parameters'}), 400
        
        file_path = "./last_names.html"
        base_list = get_last_names(file_path)
        s = generate_students_names(size=size, base_list=base_list, seed=seed)

        return jsonify({'data': str(s), "length": len(s)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/generate-first-names', methods=['GET'])
def generate_male_names():
    try:
        size = request.args.get('size')
        seed = request.args.get('seed')
        gender = request.args.get('gender')

        if not all([size, seed, gender]):
            return jsonify({'error': 'Missing parameters'}), 400
        if gender not in ['M', 'F']:
            return jsonify({'error': 'gender should be M or F'}), 400
        
        if gender == 'M':
            url = 'https://top-names.info/names.php?S=M&P=CAM'
            base_list = get_male_first_names(url)
            s = generate_students_names(size=size, base_list=base_list, seed=seed)
        elif gender == 'F':
            url = 'https://top-names.info/names.php?S=F&P=CAM'
            base_list = get_female_first_names(url)
            s = generate_students_names(size=size, base_list=base_list, seed=seed)

        return jsonify({'data': str(s), "length": len(s)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/generate-students', methods=['GET'])
def generate_students():
    try:
        males = request.args.get('males')
        females = request.args.get('females')
        seed = request.args.get('seed')

        if not all([males, females, seed]):
            return jsonify({'error': 'Missing parameters'}), 400
        
        url = 'https://top-names.info/names.php?S=M&P=CAM'
        base_list = get_male_first_names(url)
        male = generate_students_names(size=males, base_list=base_list, seed=seed)

        url = 'https://top-names.info/names.php?S=F&P=CAM'
        base_list = get_female_first_names(url)
        female = generate_students_names(size=males, base_list=base_list, seed=seed)

        url = "./last_names.html"
        base_list = get_last_names(url)
        if males is not None and females is not None:
            value = int(males) + int(females)
            last_names = generate_students_names(size=value, base_list=base_list, seed=seed)
            overall_list = concatenate_lists(last_names, male, female)

        return jsonify({'data': str(overall_list), "length": len(overall_list)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
