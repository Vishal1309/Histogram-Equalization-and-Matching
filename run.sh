( 
    python -m venv venv && 
    venv/Scripts/activate && 
    dao/dataset.py && 
    !unzip -q dataset.zip
    !rm -rf dataset.zip
    src/inBuiltEqualization.py &&
    src/myHistEqualization.py &&
    src/CompareEqualization.py && 
    src/inBuiltMatching.py &&
    src/myHistMatching.py &&
    src/CompareMatching.py &&
    src/CheckingOptimization.py
)