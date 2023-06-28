python self_instruct/generate_instances.py \
    --batch_dir data/gpt3_generations/ \
    --input_file machine_generated_instructions.jsonl \
    --output_file machine_generated_instances.jsonl \
    --max_instances_to_gen 5 \
    --engine "davinci" \
    --request_batch_size 5  \
    --api_key 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