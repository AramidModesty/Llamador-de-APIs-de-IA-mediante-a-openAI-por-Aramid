chat="""
    ChatCompletion(
        id='gen-1793409390-VLoCfbnklBRIxuvl9RBe',
        choices=[Choice(
                    finish_reason='stop',
                    index=0,
                    logprobs=None,
                    message=ChatCompletionMessage(
                        content='I am an AI language model trained by researchers from NVIDIA. I don’t have a physical body, personal experiences, or consciousness—I exist as software designed to process and generate text.\n\nI can help with things like answering questions, writing and editing, coding, brainstorming, summarizing information, and explaining concepts. How can I assist you today?',
                        refusal=None,
                        role='assistant',
                        annotations=None,
                        audio=None,
                        function_call=None,
                        tool_calls=None,
                        reasoning='The user is asking "Who are you?" This is a straightforward question about my identity as an AI assistant. I should provide a clear, concise, and honest answer about being an AI language model trained by researchers from NVIDIA.\n\nKey points to cover:\n- I am an AI assistant\n- Trained by researchers from NVIDIA\n- I don\'t have a physical form, personal experiences, or consciousness\n- I can help with various tasks (answering questions, writing, coding, analysis, etc.)\n- I should avoid claiming to be human or having feelings/identity in the human sense\n\nI should be helpful, humble, and accurate. No need to overcomplicate it.',
                        reasoning_details=[
                            {
                                'type': 'reasoning.text',
                                'text': 'The user is asking "Who are you?" This is a straightforward question about my identity as an AI assistant. I should provide a clear, concise, and honest answer about being an AI language model trained by researchers from NVIDIA.\n\nKey points to cover:\n- I am an AI assistant\n- Trained by researchers from NVIDIA\n- I don\'t have a physical form, personal experiences, or consciousness\n- I can help with various tasks (answering questions, writing, coding, analysis, etc.)\n- I should avoid claiming to be human or having feelings/identity in the human sense\n\nI should be helpful, humble, and accurate. No need to overcomplicate it.',
                                'format': 'unknown',
                                'index': 0
                            }
                        ]
                    ),
                native_finish_reason='stop')
            ],
        created=1793409390,
        model='nvidia/nemotron-3.5-super-vl:free',
        object='chat.completion',
        metadata=None,
        moderation=None,
        service_tier=None,
        system_fingerprint=None,
        usage=CompletionUsage(
            completion_tokens=214,
            prompt_tokens=20,
            total_tokens=234,
            completion_tokens_details=CompletionTokensDetails(
                accepted_prediction_tokens=None,
                audio_tokens=0,
                reasoning_tokens=140,
                rejected_prediction_tokens=None,
                text_tokens=None,
                image_tokens=0
            ),
            prompt_tokens_details=PromptTokensDetails(
                audio_tokens=0,
                cache_write_tokens=0,
                cached_tokens=0,
                image_tokens=None,
                text_tokens=None,
                video_tokens=0
            ),
            cost=0,
            is_byok=False,
            cost_details={'upstream_inference_cost': 0,
                'upstream_inference_prompt_cost': 0,
                'upstream_inference_completions_cost': 0
            }
        ),
        provider='Nvidia'
    )
""".replace("(","{").replace(")","}").replace("=",":")

chat="""ChatCompletion{
        id:'gen-1793409390-VLoCfbnklBRIxuvl9RBe',
        choices:[Choice{
                    finish_reason:'stop',
                    index:0,
                    logprobs:None,
                    message:ChatCompletionMessage{
                        content:'I am an AI language model trained by researchers from NVIDIA. I don’t have a physical body, personal experiences, or consciousness—I exist as software designed to process and generate text.

I can help with things like answering questions, writing and editing, coding, brainstorming, summarizing information, and explaining concepts. How can I assist you today?',
                        refusal:None,
                        role:'assistant',
                        annotations:None,
                        audio:None,
                        function_call:None,
                        tool_calls:None,
                        reasoning:'The user is asking "Who are you?" This is a straightforward question about my identity as an AI assistant. I should provide a clear, concise, and honest answer about being an AI language model trained by researchers from NVIDIA.

Key points to cover:
- I am an AI assistant
- Trained by researchers from NVIDIA
- I don't have a physical form, personal experiences, or consciousness
- I can help with various tasks {answering questions, writing, coding, analysis, etc.}
- I should avoid claiming to be human or having feelings/identity in the human sense

I should be helpful, humble, and accurate. No need to overcomplicate it.',
                        reasoning_details:[
                            {
                                'type': 'reasoning.text',
                                'text': 'The user is asking "Who are you?" This is a straightforwardquestion about my identity as an AI assistant. I should provide a clear, concise, and honest answer about being an AI language model trained by researchers from NVIDIA.

Key points to cover:
- I am an AI assistant
- Trained by researchers from NVIDIA
- I don't have a physical form, personal experiences, or consciousness
- I can help with various tasks {answering questions, writing, coding, analysis, etc.}
- I should avoid claiming to be human or having feelings/identity in the human sense

I should be helpful, humble, and accurate. No need to overcomplicate it.',
                                'format': 'unknown',
                                'index': 0
                            }
                        ]
                    },
                native_finish_reason:'stop'}
            ],
        created:1793409390,
        model:'nvidia/nemotron-3.5-super-vl:free',
        object:'chat.completion',
        metadata:None,
        moderation:None,
        service_tier:None,
        system_fingerprint:None,
        usage:CompletionUsage{
            completion_tokens:214,
            prompt_tokens:20,
            total_tokens:234,
            completion_tokens_details:CompletionTokensDetails{
                accepted_prediction_tokens:None,
                audio_tokens:0,
                reasoning_tokens:140,
                rejected_prediction_tokens:None,
                text_tokens:None,
                image_tokens:0
            },
            prompt_tokens_details:PromptTokensDetails{
                audio_tokens:0,
                cache_write_tokens:0,
                cached_tokens:0,
                image_tokens:None,
                text_tokens:None,
                video_tokens:0
            },
            cost:0,
            is_byok:False,
            cost_details:{'upstream_inference_cost': 0,
                'upstream_inference_prompt_cost': 0,
                'upstream_inference_completions_cost': 0
            }
        },
        provider:'Nvidia'
    }
"""


