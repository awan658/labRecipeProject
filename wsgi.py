from recipe import create_app

app = create_app()

@app.route('/')
def show_layout():
    return render_template('index.html')

if __name__ == "__app__":
    main()
    app.run(debug=True, host='localhost', port=5000, threaded=False)
